#!/usr/bin/env python

'''
tests all files in this repo for basic compliance with the NeXus standard (per 2016 NIAC)


USAGE

To update the compliance report in this repo::

    ./critique.py | tee critique.md

Notes:  

* use h5py 2.10 or higher 
  (https://github.com/nexusformat/exampledata/pull/14#issuecomment-577305522)
* This code is compliant with both python 2 and python 3
* This code does not perform a full validation of NeXus data files.
  It only checks that a given file can be opened by h5py
  and has at least one *NXentry* group.
  
  Tests for this structure 
  (exact name of *entry01* is not required)::
        
    <file_root>:
        entry01 (NXentry)
            ...     # content not checked at this level
        ...     # additional content not checked at this level
        
  :see: http://wiki.nexusformat.org/2014_How_to_find_default_data
  :see: https://www.nexusformat.org/NIAC2016Minutes.html#nxdata

'''


import datetime
import h5py
import numpy
import pyRestTable
import os
import sys
import xml.etree.ElementTree as ET


def isNeXusGroup(obj, NXtype):
    """is `obj` a NeXus group?"""
    nxclass = None
    if isinstance(obj, h5py.Group):
        if "NX_class" not in obj.attrs:
            return False
        try:
            nxclass = obj.attrs['NX_class']
        except Exception as exc:
            # print(exc)
            return False
        if isinstance(nxclass, numpy.ndarray):
            nxclass = nxclass[0]
    
    if isinstance(nxclass, bytes) and not isinstance(nxclass, str):
            nxclass = nxclass.decode()
    return nxclass == NXtype


class Critic(object):
    '''
    describe a file in terms of NeXus compliance.
    Each method starting with "test_" will contribute a column to the results table.
    
    :param str path: absolute or relative path to the file directory
    :param str fname: (absolute or relative path and) name of file
    '''
    
    def __init__(self, path=None, fname=None):
        self.path = path
        self.fname = fname
        self.NXentry_nodes = []
        self.filetype = "unrecognised"
        self.test_results = []

        test_bank = [func for func in dir(Critic) if callable(getattr(Critic, func)) and func.startswith("test_")]
        for t in test_bank:
            try:
                self.test_results += [getattr(self, t)(path, fname)]
            except:
                self.test_results += ["error"]
    
    def find_NX_class_nodes(self, parent, nx_class = 'NXentry'):
        '''identify the NXentry (or as specified) nodes'''
        node_list = []
        for node in parent.values():
            if isNeXusGroup(node, nx_class):
                node_list.append(node)
        return node_list
    
### Each method starting with "test_" will contribute a column to the results table.
### The tests are conducted in alphabetical order.
### Note that each test can write attributes onto self for later tests to use.
    def test_01_FileType(self, path, fname):
        if path is None and fname is None:
            return "File Type"
        try:
            with h5py.File(os.path.join(self.path, self.fname), mode="r") as root:
                self.filetype = "HDF5"
        except IOError:
            pass        # cannot open with HDF5
        
        if self.filetype == "unrecognised": # try to ID as XML
            try:
                tree = ET.parse(os.path.join(self.path, self.fname))
                self.filetype = "XML"
            except ET.ParseError:
                pass        # cannot open as XML
        
        if self.filetype == "unrecognised": # try to ID as HDF4
            MAGIC_HDF4 = b'\x0e\x03\x13\x01\x00\xc8\x00\x00'
            with open(os.path.join(self.path, self.fname), "rb") as file:
                sig = file.read(8)
            if sig == MAGIC_HDF4:
                self.filetype = "HDF4"
        return self.filetype

#    def test_01a_FileHeader(self, path, fname):
#        if path is None and fname is None:
#            return "Header"
#        with open(os.path.join(self.path, self.fname), "rb") as file:
#            file.seek(0)
#            sig = file.read(8)
#        return ":".join("{:02x}".format(x) for x in bytearray(sig))

    def test_02_NXentryCount(self, path, fname):
        if path is None and fname is None:
            return "NXentry Count"
        if self.filetype == "HDF5":
            with h5py.File(os.path.join(self.path, self.fname), mode="r") as root:
                NXentry_nodes = self.find_NX_class_nodes(root, "NXentry")
                self.nNXentry = len(NXentry_nodes)
            if self.nNXentry == 0:
                return "not NeXus"
        elif self.filetype == "XML":
            self.nNXentry = "*"
        elif self.filetype == "HDF4":
            self.nNXentry = "*"
        else:
            self.nNXentry = "-"
        return self.nNXentry

    def test_03_ApplicationDefinition(self, path, fname):
        if path is None and fname is None:
            return "Application Def's"
        if self.filetype == "HDF5":
            if self.nNXentry < 1:
                AppDefList = "-"
            else:
                ad_list = set() # like a list, but only keep unique strings
                with h5py.File(os.path.join(self.path, self.fname), mode="r") as root:
                    NXentry_nodes = self.find_NX_class_nodes(root, "NXentry")
                    for entry in NXentry_nodes:
                        subentry_list = self.find_NX_class_nodes(entry, "NXsubentry")
                        if len(subentry_list) == 0:
                            if 'definition' in list(entry):
                                ad_list.add(str(entry['definition'][0], encoding='utf-8')) #definition found in NXentry
                        else:
                            for sub in subentry_list:
                                ad_list.add(str(sub['definition'][0], encoding='utf-8')) #definition found in NXsubentry
                if len(ad_list) == 0:
                    AppDefList = "None found"
                else:
                    AppDefList = ",".join(ad_list)
        elif self.filetype == "XML":
            AppDefList = "*"
            
        elif self.filetype == "HDF4":
            AppDefList = "*"
            
        else:
            AppDefList = "-"
            
        return AppDefList


class Registrar(object):
    '''keep track of critiqued files in an internal dictionary'''

    def __init__(self):
        self.db = {}
        self.test_bank = [
          func
          for func in dir(Critic)
          if callable(getattr(Critic, func)) and func.startswith("test_")
          ]
        self.table_labels = ["path", "file"] + Critic().test_results


    def add(self, path, critic):
        '''add new critique to the database'''
        if critic.fname is None:
            return
        if path not in self.db:
            self.db[path] = {}
        self.db[path][critic.fname] = critic
    
    def report(self):
        table = pyRestTable.Table()
        table.labels = self.table_labels
        for path, flist in sorted(self.db.items()):
            for fname, critique in sorted(flist.items()):
                table.addRow(["`"+path+"`", "`"+fname+"`"]+ critique.test_results)
            
        print(table.reST(fmt="markdown"))


def walk_function(registrar, path, files):
    '''
    called for each directory traversed
    
    :param obj registrar: instance of Registrar(), database of analyzed files
    :param str path: subdirectory name
    :param [str] files: list of files in *path* directory
    '''
    if path.find('.git') > -1:      # skip the Git VCS directory
        return
    skip_extensions = ['.txt', '.py', '.rst', '.md', '.in']
    for nm in files:
        if os.path.splitext(nm)[1] not in skip_extensions and nm[0] != '.': # skip other types of file
                registrar.add(path, Critic(path, nm))


def main(path=None):
    '''traverse a directory and describe how each file conforms to NeXus'''
    registrar = Registrar()
    paths = [path or os.path.dirname(__file__) or '.']
    while len(paths) > 0:
        path = paths.pop()
        for subdir, dir_list, file_list in os.walk(path):
            if os.path.basename(subdir) in (".vscode", ".git"):
                continue
            paths += [
                os.path.join(subdir, p) 
                for p in dir_list]
            walk_function(registrar, subdir, file_list)
    
    print("# Critique of *exampledata* files")
    print("")
    print("* date: %s" % datetime.datetime.now())
    print("* h5py version: %s" % h5py.__version__)
    print("* unimplemented test cases are marked in the table with an asterisk")
    print("")
    registrar.report()


if __name__ == '__main__':
    main()
