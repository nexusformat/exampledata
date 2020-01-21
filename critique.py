#!/usr/bin/env python

'''describe NeXus compliance of files in this repository'''


import h5py
import numpy
import os
import sys


def isHdf5Group(obj):
    """is `obj` an HDF5 Group?"""
    return isinstance(obj, h5py.Group)


def isNeXusGroup(obj, NXtype):
    """is `obj` a NeXus group?"""
    nxclass = None
    if isHdf5Group(obj):
        if "NX_class" not in obj.attrs:
            return False
        try:
            nxclass = obj.attrs.get('NX_class', None)
        except Exception as exc:
            # print(exc)
            return False
        if isinstance(nxclass, numpy.ndarray):
            nxclass = nxclass[0]
    return nxclass == str(NXtype)


def is_spec_file(fullname):
    return False    # see spec2nexus.spec.is_spec_file()


class Critic(object):
    '''
    describe a file in terms of NeXus compliance
    
    :param str fname: (absolute or relative path and) name of file
    '''
    
    def __init__(self, path, fname):
        self.path = None
        self.fname = None
        self.hdf5 = None
        self.NXentry_nodes = []
        self.isNeXus = False

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
        
        # alternative to find_self.NXentry_NXdata_nodes(), deeper analysis
        # this code only checks for NXentry/NXdata/<data>/@signal=1
        self.isNeXus = self.isHDF5(fullname) and (is_spec_file(fullname) or self.niac2014Compliance(fullname))

        # is it an HDF5 file?
        if not self.openHDF5(fullname):
            return

        # TODO: make lists of
        #    all field names
        #    group names
        #    nx_class types
        # TODO: check all field names
        #    field names for fit to the regexp
        #    field names for correct codepage
        #    strings for correct codepage

        # finally: close the HDF5 file
        self.hdf5.close()
    
    def describe_file(self):
        s = 'HDF5 file'
        if self.hdf5 is None:
            return 'not ' + s
        if self.isNeXus:
            s = 'NeXus ' + s
        if len(self.NXentry_nodes) > 0:
            s += ', %d **NXentry** group' % len(self.NXentry_nodes)
            if len(self.NXentry_nodes) > 1:
                s += 's'
        return s

    def __str__(self, *args, **kwargs):
        return self.describe_file()
    
    def isHDF5(self, fname):
        '''is this an HDF5 file?'''
        if not self.openHDF5(fname):
            return False
        self.hdf5.close()
        return True

    def openHDF5(self, fname):
        '''try to open the file as HDF5'''
        try:
            self.hdf5 = h5py.File(fname, 'r')
        except IOError:
            return False
        return True    
    
    def find_NX_class_nodes(self, parent = None, nx_class = 'NXentry'):
        '''identify the NXentry (or as specified) nodes'''
        parent = parent or self.hdf5
        node_list = []
        for node in parent.values():
            if isNeXusGroup(node, nx_class):
                node_list.append(node)
        return node_list
    
    def niac2014Compliance(self, fullname):
        '''
        tests file for compliance with NIAC2014 agreement on how to find the plottable data
        
        .. note::  This test is not robust.
           
           * It does not test every NXdata group for compliance 
             with the **NIAC2014** method.
           * It does not test each NXentry for at least one NXdata 
             group compliant with the **NIAC2014** method.
           * It does not detect a file with mixed structure, 
             both ``signal=1`` and **NIAC2014** methods.

        Tests data file for this structure (as agreed at 2014 NIAC meeting)::
        
            <file_root>:
                @default = "entry01"      (only needed to resolve ambiguity)
                entry01 (NXentry)
                    @default = "data02"   (only needed to resolve ambiguity)
                    data01 (NXdata)
                        ...
                    data02 (NXdata)
                        @signal = "data1"
                        data1
                        data2
                entry02 (NXentry)
                    ...
        
        :see: http://wiki.nexusformat.org/2014_How_to_find_default_data
        '''
        #------------------------------------------
        def get_default(group, subgroupclass):
            subgroups = self.find_NX_class_nodes(group, nx_class = subgroupclass)

            # MUST have at least one of subgroupclass
            if len(subgroups) > 0:

                # if "default" attribute is supplied
                if 'default' in group.attrs:
                    subgroupname = group.attrs['default']
                    if subgroupname in group:
                        return group[subgroupname]
    
                # fallback case, 'default' attribute is optional
                if len(subgroups) == 1:
                    return subgroups[0]

            return False
        #------------------------------------------
        # TODO: make test more robust
        compliance = False
        if self.openHDF5(fullname):
            entry = get_default(self.hdf5, 'NXentry')
            if entry:
                data = get_default(entry, 'NXdata')
                if data:
                    if 'signal' in data.attrs:
                        signalname = data.attrs['signal']
                        compliance = signalname in data
            self.hdf5.close()

        return compliance


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
            print '\n' + path + '\n' + '+'*len(path)
            for fname, critique in sorted(flist.items()):
                print ':'+fname+': ', str(critique)


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
    path = path or os.path.dirname(__file__)
    os.path.walk(path, walk_function, registrar)
    registrar.report()
    # TODO: should modify the README.rst
    #    after the line that reads:
    #    .. --- CRITIQUE report starts after this line ---


if __name__ == '__main__':
    main()
