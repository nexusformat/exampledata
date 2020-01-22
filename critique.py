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
    describe a file in terms of NeXus compliance
    
    :param str fname: (absolute or relative path and) name of file
    '''
    
    def __init__(self, path, fname):
        self.path = None
        self.fname = None
        self.NXentry_nodes = []
        self.filetype = "not HDF5 file"

        # can the file be found?
        fullname = os.path.join(path, fname)
        if not os.path.exists(fullname):
            return

        # Is it really a file?
        if not os.path.isfile(fullname):
            return
        
        # ok, passes basic qualifications, proceed
        self.path = path
        self.fname = fname

        try:
            with h5py.File(fullname, mode="r") as root:
                self.filetype = "HDF5 file"
                self.NXentry_nodes = self.find_NX_class_nodes(root, "NXentry")
                if len(self.NXentry_nodes) > 0:
                    self.filetype = "NeXus HDF5 file"
        except IOError:
            pass        # cannot open with HDF5

        # no deeper validation of the NeXus data file
    
    def describe_file(self):
        s = self.filetype
        if len(self.NXentry_nodes) > 0:
            s += ', %d **NXentry** group' % len(self.NXentry_nodes)
            if len(self.NXentry_nodes) > 1:
                s += 's'
        return s

    def __str__(self, *args, **kwargs):
        return self.describe_file() 
    
    def find_NX_class_nodes(self, parent, nx_class = 'NXentry'):
        '''identify the NXentry (or as specified) nodes'''
        node_list = []
        for node in parent.values():
            if isNeXusGroup(node, nx_class):
                node_list.append(node)
        return node_list


class Registrar(object):
    '''keep track of critiqued files in an internal dictionary'''

    def __init__(self):
        self.db = {}

    def add(self, path, critic):
        '''add new critique to the database'''
        if critic.fname is None:
            return
        if path not in self.db:
            self.db[path] = {}
        self.db[path][critic.fname] = critic
    
    def report(self):
        for path, flist in sorted(self.db.items()):
            table = pyRestTable.Table()
            table.labels = ["file", "critique"]
            for fname, critique in sorted(flist.items()):
                table.addRow(("``"+fname+"``", critique))
            
            print("\n## path: " + path + "\n")
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
    for nm in files:
        registrar.add(path, Critic(path, nm))


def main(path = None):
    '''traverse a directory and describe how each file conforms to NeXus'''
    registrar = Registrar()
    paths = [path or os.path.dirname(__file__)]
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
    registrar.report()


if __name__ == '__main__':
    main()
