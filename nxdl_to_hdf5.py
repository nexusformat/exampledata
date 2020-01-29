#!/usr/bin/env python

import time
import datetime
from time import localtime
import xmltodict
import glob
import pkg_resources
import os
import simplejson as json
import numpy as np

def _string_attr(nxgrp, name, sdata):
    '''
    used to create string attributes
    '''
    if (nxgrp is None):
        return
    nxgrp.attrs[name] = sdata


def _list_attr(nxgrp, name, lstdata):
    '''

    used to create list attributes
    '''
    #print(nxgrp, name, lstdata)
    if (nxgrp is None):
        return
    if (name in list(nxgrp.attrs.keys())):
        nxgrp.attrs[name][()] = lstdata
    else:
        nxgrp.attrs[name] = lstdata


def _group(nxgrp, name, nxdata_type):
    '''
    create a group
    '''
    if (name == ''):
        return
    grp = nxgrp.create_group(name)
    _string_attr(grp, 'NX_class', nxdata_type)
    return (grp)

def _dataset(nxgrp, name, data, nxdata_type, nx_units='NX_ANY', dset={}):
    '''
    create a dataset, apply compression if the data is an array
    '''
    # grp = nxgrp.create_dataset(name=name, data=data, maxshape=None)
    if (type(data) == np.ndarray):
        grp = nxgrp.create_dataset(name=name, data=data, maxshape=None, compression="gzip")
    else:
        #print('name[%s] data[%s]' % (name, data))
        if(data is None):
            data = ''
            # if(name in list(nxgrp.keys())):
            #     print()
        grp = nxgrp.create_dataset(name=name, data=data, maxshape=None)
    _string_attr(grp, 'NX_class', nxdata_type)
    if (type(nx_units) is dict):
        _string_attr(grp, 'NX_units', nx_units['units'])
    else:
        _string_attr(grp, 'NX_units', nx_units)
    if ('doc' in list(dset.keys())):
        _string_attr(grp, 'doc', dset['doc'])
    return (grp)

def xml_class_to_dict(xmlstr):
    '''
    wraps calls that take an xmlstring and turns it into a dict
    '''
    resp_ordereddict = xmltodict.parse(xmlstr)
    resp_json = json.dumps(resp_ordereddict, indent=4, sort_keys=True)
    resp_dict = json.loads(resp_json)
    return(resp_dict)

def build_class_dict(class_dir='base_classes', desired_class=None, defdir=None):
    '''
    build a nxdl definition into a dict

        class_dir: either 'applications' or 'base_classes'
        desired_class: the name of a desired class definition such as 'NXstxm', if left as None then all class definitions\
                will be returned.
        defdir: if the definitions are located somewhere other than in a subdir of nexpy

    '''
    if(defdir is None):
        class_path = pkg_resources.resource_filename('nexpy', 'definitions/%s' % class_dir)
    else:
        class_path = os.path.join(defdir, class_dir)

    nxdl_files = list(map(os.path.basename, glob.glob(os.path.join(class_path, '*.nxdl.xml'))))
    dct = {}
    if(desired_class):
        nxdl_files = [os.path.join(class_path, '%s.nxdl.xml' % desired_class)]

    for nxdl_file in nxdl_files:
        xmlstr = open(os.path.join(class_path, nxdl_file)).read()
        class_nm = nxdl_file.replace('.nxdl.xml', '')
        if(class_nm.find(os.path.sep) > -1):
            class_nm = class_nm.split(os.path.sep)[-1]
        resp_dict = xml_class_to_dict(xmlstr)
        dct[class_nm] = resp_dict
    return(dct)

def build_trimmed_class_dict(class_dir='base_classes', desired_class=None):
    '''
    wraps several functions to take the name of a class definition that the caller wants and turns it into a dict
    '''
    dct = build_class_dict(class_dir, desired_class)

    final_dct = {}
    for k, v in dct.items():
        _dct = class_to_trimmed_dict(v)
        final_dct[k] = _dct
    return(final_dct)

def is_occurs_true(occrs):
    if(occrs.find('1') > -1):
        return(True)
    else:
        return(False)

def class_to_trimmed_dict(cls):
    '''
    function takes a resulting dict from xmltodict and creates a reduced dict that contains the minimal dict that
    is later used to create the hdf5 file, in the future the hdf5 will likely be created by this function directly.
    '''
    dct = {}
    name = None
    if('definition' in cls.keys()):
        if ('@name' in cls['definition'].keys()):
            name = cls['definition']['@name']
            dct[name] = {}
            dct = dct[name]

        else:
            pass
        items = cls['definition'].items()
    else:
        if('@name' in cls.keys()):
            name = cls['@name']
            dct[name] = {}
            dct[name]['nx_type'] = cls['@type']

        else:
            pass
        items = cls.items()
    required = False
    for k, v in items:
        #print('found key [%s]' % k)
        if (k.find('@maxOccurs') > -1):
            pass
        elif (k.find('@minOccurs') > -1):
            if(v.find('1') > -1):
                required = True
        elif (k.find('symbols') > -1):
            dct['symbols'] = {}
            if('doc' in dct['symbols'].keys()):
                dct['symbols']['doc'] = v['doc']
            dct['symbols']['symbol'] = []
            if(type(v['symbol']) is dict):
                v['symbol'] = [v['symbol']]
            for _sym in v['symbol']:
                dct['symbols']['symbol'].append([_sym['@name'], _sym['doc']])

        elif (k.find('@category') > -1):
            pass
        elif (k.find('@name') > -1):
            #name = v
            #dct[name] = {}
            pass
        elif (k.find('@type') > -1):
            pass
        elif (k.find('@extends') > -1):
            pass
        elif (k.find('@xmlns:xsi') > -1):
            pass
        elif (k.find('@xsi:schemaLocation') > -1):
            pass
        elif (k.find('@xmlns') > -1):
            pass
        elif (k.find('@svnid') > -1):
            pass

        elif (k.find('attribute') > -1): ########################### ATTRIBUTEs ################################
            pass

        elif(k.find('doc') > -1): ########################### DOC #################################
            dct['doc'] = v

        elif (k.find('group') > -1): ########################### GROUPs #################################

            cntr = 0
            #single groups are not lists so make them one
            if (type(v) is dict):
                v = [v]
            for d in v:
                #make new group here

                if ('@minOccurs' in d.keys()):
                    grp_minoccurs = d['@minOccurs']
                else:
                    grp_minoccurs = '1' #default

                if ('@maxOccurs' in d.keys()):
                    grp_maxoccurs = d['@maxOccurs']
                else:
                    grp_maxoccurs = 0 #default

                if('@name' in d.keys()):
                    # if(d['@name'].find('NXinstrument') > -1):
                    #     print()
                    if (d['@name'].find('NX_') > -1):
                        # its a nexus data type
                        dct[d['@name']] = {'nx_type': d['@type'], '_dvals_': '', 'required': is_occurs_true(grp_minoccurs)}
                    else:
                        # its a nexus class type
                        dct[d['@name']] = {'nx_class': d['@type'], '_dvals_': '', 'required': is_occurs_true(grp_minoccurs)}
                        dct[d['@name']].update(class_to_trimmed_dict(d))

                        # _d.update({'nx_class': d['@type']})
                        # dct.update(_d)
                else:
                    # @name does not exist in d
                    _dct = class_to_trimmed_dict(d)
                    #nm = '%s_%d' % (d['@type'].replace('NX',''), cntr)
                    nm = '%s' % d['@type']
                    # if (nm.find('NXinstrument') > -1):
                    #     print()
                    cntr += 1
                    if(len(_dct) < 1):
                        if(d['@type'].find('NX_') > -1):
                            #its a nexus data type
                            dct[nm] = {'nx_type': d['@type'], '_dvals_': '', 'required': is_occurs_true(grp_minoccurs)}
                        else:
                            #its a nexus class type
                            nm = nm.replace('NX','')
                            dct[nm] = {'nx_class': d['@type'], '_dvals_': '', 'required': is_occurs_true(grp_minoccurs)}
                    else:
                        if(d['@type'].find('NX') > -1):
                            clss_nm = d['@type']
                        dct[nm] = class_to_trimmed_dict(d)
                        dct[nm].update({'required': is_occurs_true(grp_minoccurs)})


        elif (k.find('link') > -1): ########################### LINKs #################################
            links = []
            #link section should hold a list of dicts or a single dict
            if (type(v) is dict):
                v = [v]
            for item in v:
                links.append([item['@name'], item['@target'].replace(' ', '_')] )

            if (len(links) > 0):
                dct['links'] = links
                #print(links)

        elif(k.find('field') > -1): ########################### FIELDs #################################

            #walk the fields,
            # ensure single fields are lists as well

            if (type(v) is dict):
                v = [v]
            for item in v:
                fld_name = 'NO_NAME'
                fld_doc = None
                axis = None
                attrs = {}
                enums = []
                fld_rqrd = False
                _type = 'NX_CHAR'
                units = None
                if(type(item) is dict):
                    fld_name = item['@name']
                    # if (fld_name.find('energy') > -1):
                    #     print()
                    # print('field [%s]' % fld_name)
                    if ('enumeration' in item.keys()):
                        if (type(item['enumeration']['item']) is dict):
                            item['enumeration']['item'] = [item['enumeration']['item']]
                        #print(name)
                        for e_item in item['enumeration']['item']:
                            if(type(e_item) is dict):
                                enums.append(e_item['@value'])
                        #print(enums)
                    if('@type' in item.keys()):
                        _type = item['@type']
                    if ('@units' in item.keys()):
                        units = item['@units']
                    if ('doc' in item.keys()):
                        if(item['doc'] is not None):
                            fld_doc = item['doc']
                    if ('@axis' in item.keys()):
                        axis = item['@axis']

                    if ('@maxOccurs' in item.keys()):
                        pass
                    if ('@minOccurs' in item.keys()):
                        if (item['@minOccurs'].find('1') > -1):
                            fld_rqrd = True
                        else:
                            fld_rqrd = False
                    else:
                        #if there is no min specified then it defaults to required
                        fld_rqrd = True

                    if('attribute' in item.keys()):
                        for a_item in item['attribute']:
                            if(type(a_item) is dict):
                                if('doc' in a_item.keys()):
                                    attrs[a_item['@name']] = a_item['doc']
                                else:
                                    attrs[a_item['@name']] = ''

                #dont include everything in final dct

                dct[fld_name] = {}
                if(fld_doc):
                    dct[fld_name]['doc'] = fld_doc

                if(axis):
                    dct[fld_name]['axis'] = axis

                if(_type):
                    dct[fld_name]['nx_type'] = _type
                else:
                    dct[fld_name]['nx_type'] = 'NX_CHAR'
                    _type = 'NX_CHAR'

                if(units):
                    dct[fld_name]['nx_units'] = units
                else:
                    units = 'NX_ANY'

                if(len(attrs) > 0):
                    dct[fld_name]['attrs'] = attrs

                if(len(enums) > 0):
                    dct[fld_name]['enums'] = enums
                    dct[fld_name]['_dvals_'] = enums[0]
                else:
                    dct[fld_name]['_dvals_'] = get_nx_data_by_type(_type)

                dct[fld_name]['required'] = fld_rqrd


    return(dct)

def get_nx_data_by_type(nx_type, size=1):
    '''
    return a piece of data to put in demo file
    '''
    if(nx_type.find('NX_CHAR') > -1):
        return('')
    elif(nx_type.find('NX_FLOAT') > -1):
        return(0.0)
    elif (nx_type.find('NX_INT') > -1):
        return (0)
    elif (nx_type.find('NX_BOOLEAN') > -1):
        return (False)
    elif (nx_type.find('NX_DATE_TIME') > -1):
        return(make_timestamp_now())
    elif (nx_type.find('NX_NUMBER') > -1):
        return (0)
    elif (nx_type.find('NX_POSINT') > -1):
        return (1)
    elif (nx_type.find('NX_UINT') > -1):
        return (0)


def nx_dict_as_nf(nf, dct, num_tabs=0):
    '''
    walk dict creating h5 entries
    :param nf:
    :param dct:
    :return:
    '''
    fld_skip_list = ['nx_class', 'required', '_dvals_']
    for k, v in dct.items():
        # if(k.find('NXinstrument') > -1):
        #     print()
        if(type(v) is dict):
            s = ''
            for t in range(num_tabs):
                s += '\t'
            units = 'NX_ANY'
            if('nx_type' in v.keys()):
                #the other code has stuff for adding enum group?
                if('nx_units' in v.keys()):
                    units = v['nx_units']

                if(nf.name.find(k) < 0):
                    #skip creating the group name as a dataset
                    g = _dataset(nf, k, v['_dvals_'], v['nx_type'], nx_units=units)
                    if ('doc' in v.keys()):
                        _string_attr(g, 'doc', ' '.join(v['doc'].split()))
                    if ('axis' in v.keys()):
                        _string_attr(g, 'axis', v['axis'])
                    if ('enums' in v.keys()):
                        _list_attr(g, 'enumerations', v['enums'])
                        g[()] = v['enums'][0]
                    if ('required' in list(v.keys())):
                        _string_attr(g, 'required', v['required'])

            elif(k.find('symbol') > -1):
                for i in v['symbol']:
                    nm, dat = i
                    _string_attr(nf, nm, dat)
            elif (k.find('links') > -1):
                    pass
            else:
                if ('nx_class' in v.keys()):
                    nxgrp = _group(nf, k, v['nx_class'])
                else:

                    #print('CREATING GROUP [%s]' % k.replace('NX', '').upper())
                    nxgrp = _group(nf, k.replace('NX', '').upper() , k)

                _string_attr(nxgrp, 'required', v['required'])
                nx_dict_as_nf(nxgrp, v, num_tabs=num_tabs+1)
        else:

            if(v is None):
                v = ''
            if(k.find('doc') > -1):
                #remove the tabs and new lines from doc string
                v = ' '.join(v.split())
                _string_attr(nf, 'doc', v)
                continue

            if (k.find('links') > -1):
                #print()
                for nm, trgt in v:
                    if(nm in nf.keys()):
                        gr = nf[nm]
                    else:
                        gr = _dataset(nf, nm, 0.0, 'NX_NUMBER')
                    _string_attr(gr, '@target', trgt)

            elif (k not in fld_skip_list):
                dgrp = _dataset(nf, k, v, 'NX_CHAR')

                if(type(v) is dict):
                    if('required' in list(v.keys())):
                        _string_attr(dgrp, 'required', v['required'])


def make_timestamp_now():
    """
    create a ISO 8601 formatted time string for the current time and return it
    """
    t = datetime.datetime.now().isoformat()
    return (t)

def make_class_as_nf_file(def_subdir, clss_nm, dct):
    '''
    take a nxdl definition name and create an hdf5 file
    '''

    dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'nxdl', def_subdir)
    if(not os.path.exists(dest_dir)):
        os.makedirs(dest_dir)

    fpath = os.path.join(dest_dir, '%s.hdf5' % clss_nm)
    nf = h5py.File(fpath, 'w')
    _string_attr(nf, 'file_name', fpath)
    _string_attr(nf, 'file_time', make_timestamp_now())
    nx_dict_as_nf(nf, dct)
    nf.close()
    print('finished exporting to [%s]' % fpath)

if __name__ == '__main__':
    import h5py

    ####################################################################################################################
    # one definition
    # class_dct = build_trimmed_class_dict('applications', desired_class='NXcanSAS')
    # for k, v in class_dct.items():
    #     make_class_as_nf_file(k, v)

    # # all definitions
    #
    #def_subdir = 'base_classes'
    #def_subdir = 'applications'
    def_subdir = 'contributed_definitions'
    class_dct = build_trimmed_class_dict(def_subdir)
    for k, v in class_dct.items():
        make_class_as_nf_file(def_subdir, k, v)

