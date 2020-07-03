
import os
import pkg_resources
import h5py
import glob
import datetime
import numpy as np
from lxml import etree
import bs4


def _string_attr(nxgrp, name, sdata):
    '''
    used to create string attributes
    '''
    sdata = sdata.replace('\t',' ')
    sdata = sdata.replace('\n', ' ')
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
    #if name of group already exists then increment name by one until it is unique
    i = 1
    _name = name
    while name in nxgrp.keys() and i < 100:
        name = _name + '_%d' % i
        i += 1

    grp = nxgrp.create_group(name)
    _string_attr(grp, 'NX_class', nxdata_type)
    return (grp)

def _dataset(nxgrp, name, data, nxdata_type, nx_units='NX_ANY', dset={}):
    '''
    create a dataset, apply compression if the data is an array
    '''
    # grp = nxgrp.create_dataset(name=name, data=data, maxshape=None)
    if (type(data) == np.ndarray):
        #print('creating np.ndarray dataset [%s]' % name)
        grp = nxgrp.create_dataset(name=name, data=data, maxshape=None, compression="gzip")
    else:
        #print('name[%s] data[%s]' % (name, data))
        if(data is None):
            data = ''
        #print('creating dataset [%s]' % name)
        grp = nxgrp.create_dataset(name=name, data=data, maxshape=None)

    _string_attr(grp, 'NX_class', nxdata_type)
    if (type(nx_units) is dict):
        _string_attr(grp, 'units', nx_units['units'])
    else:
        _string_attr(grp, 'units', nx_units)
    if ('doc' in list(dset.keys())):
        _string_attr(grp, 'doc', dset['doc'])
    return (grp)

def get_abspath(a):
    '''
    walking the parents of an xml attribute, return a list of the parent names
    '''
    #s = '/'
    l = None
    k = None
    parent = a.getparent()
    if(parent is not None):
        if('name' in a.attrib.keys()):
            k = 'name'
        elif('type' in a.attrib.keys()):
            k = 'type'
        l = get_abspath(parent)
    if (l is None):
        l = []
    if(k):
        l.append(a.attrib[k])

    if(len(l) > 0):
        if(None in l):
            l.remove(None)
        return(l)
    else:
        return([])

def abspath_lst_to_str(l):
    '''
    assemble a path string from list of names
    '''
    if l is None:
        print()
    s = '/'
    for n in l:
        s += '%s/' % fix_nx_name(n)
    return(s)

def get_children_list_of_lists(e):
    #print(str(e) + str(e.attrib))
    pth_lst = get_abspath(e)
    abspath = abspath_lst_to_str(pth_lst)
    t = e.getroottree()
    lst = [{'ptype': e.tag, 'xpath': t.getpath(e), 'abspath': abspath, 'attrib': dict(e.attrib), 'doc': e.text}]
    children = e.getchildren()
    for ch in children:
        if(len(ch.getchildren()) > 0):
            lst.append(get_children_list_of_lists(ch))
        else:
            t = ch.getroottree()
            ch_pth_lst = get_abspath(ch)
            ch_abspath = abspath_lst_to_str(ch_pth_lst)
            ptype = ch.tag
            if(ptype):
                lst.append({'ptype': ch.tag, 'xpath': t.getpath(ch), 'abspath': ch_abspath,
                            'attrib': dict(ch.attrib), 'doc': ch.text})
    return(lst)

def get_children(e):
    lists = get_children_list_of_lists(e)
    l = list(flatten(lists))
    return(l)

def flatten(lst):
    for el in lst:
        if isinstance(el, list):
            # recurse
            yield from flatten(el)
        else:
            # generate
            yield el

def get_type(d):
    if('type' not in d['attrib'].keys()):
        return('NX_CHAR')
    else:
        return(d['attrib']['type'])

def get_parent_path(pth):
    pth2 = pth.split('/')
    for p in pth2:
        if(p == ''):
            pth2.remove(p)
    p = abspath_lst_to_str(pth2[0:-1])
    return(p)

def get_min_occurs(d, category):
    '''
    a minOccurs that is not defined has different defaults depending on the type or 'category' of definition it is.
        category="base" definitions the default when there is no minOccurs defined is that they are 'optional'
        category="application" definitions the default when there is no minOccurs defined is that they are 'required'
        category="contributed" definitions the default when there is no minOccurs defined is that they are 'required'
    '''
    valid_categories = ['base', 'application', 'contributed']
    if category not in valid_categories:
        print('Error: invalid definition category [%s]' % (category))
        print('\t must be one of ', valid_categories)
        exit()
    if ('minOccurs' in d['attrib'].keys()):
        min_occurs = int(d['attrib']['minOccurs'])
        if (min_occurs > 0):
            reqd = 'true'
        else:
            reqd = 'false'
    else:
        if(category.find('application') > -1):
            #default for application definitions if no minOccurs specified
            reqd = 'true'
        else:
            # default for all other definitions if no minOccurs specified
            reqd = 'false'
    return(reqd)

def get_doc(d):
    doc = None
    if('doc' in d.keys()):
        if(type(d['doc']) is str):
            if(len(d['doc'].strip()) > 1):
                doc = d['doc']
    return(doc)

def sanity_check_dimensions(dct, sym_dct={}):
    '''
     for every dimensions spec there should be a 'rank' specified and there should be at least the same number
     of accompnying dim sections as the value specified in 'rank'
    '''

    if(type(dct) is dict):
        if('attrib' in dct.keys()):
            if('rank' in dct['attrib'].keys()):
                if(has_numbers(dct['attrib']['rank'])):
                    rank = int(dct['attrib']['rank'])
                else:
                    print(
                        '\t\tError: rank designation is using a symbol that has not been defined in Symbols table or it is a comment')
                    print('\t\t [%s]' % (dct['attrib']['rank']))
                    return(False)

                if(rank <= len(dct['attrib']['dim'])):
                    return(True)
                else:
                    print('\t\tError: Incorrect number of dim sections for this dimensions specification, should be at least [%d] found [%d]' %  (rank, len(dct['attrib']['dim'])))
                    print('\t\t[%s]' % dct['abspath'])
                    return (False)
            else:
                #print('\t\tError: dimensions must specify a rank, this does not >', dct)
                return(False)
        else:
            return(False)
    else:
        return(False)

def get_nx_data_by_type(nx_type, dimensions=None, sym_dct={}):
    '''
    using the passed in type, return some sample data of the correct type, dimension and size if an array
    '''
    errors = False
    data = None
    use_dims = False
    if( sanity_check_dimensions(dimensions, sym_dct)):
        if (dimensions and 'attrib' in dimensions.keys() and len(dimensions['attrib']['dim']) > 0):
            dimensions = dimensions['attrib']
            arr = []
            #first create an array of rank dimensions
            if('rank' not in dimensions.keys()):
                if ('value' in dimensions.keys()):
                    val = int(dimensions['value'])
                    arr.append(val)
                else:
                    arr.append(1)
            else:
                #check if symbol was used in defining a rank
                if(has_numbers(dimensions['rank'])):
                    if 'value' in dimensions.keys():
                        if not has_numbers(dimensions['value']):
                            if dimensions['value'] not in sym_dct.keys():
                                print('\t-Most likely this [%s] should be a symbol but has not been defined in the Symbols table as one' % dimensions['value'])
                            rank = 1
                            sym_dct[dimensions['value']] = rank
                        else:
                            rank = int(dimensions['value'])
                    else:
                        rank = 1
                    rank = int(dimensions['rank'])
                    for r in range(0, rank):
                        #verify length of dim as teh number of dim entries must equal rank size
                        if (len(dimensions['dim']) < rank):
                            print('\t-Invalid NXDL file, the number of DIM entries must equal the size of specified rank [%d]' % rank)
                            errors = True
                            return(None)
                        # check if symbol was used in defining a dim value
                        if('value' not in dimensions['dim'][r].keys()):
                            print('\t\tError, there is no [value] key in dim specification' , dimensions['dim'][r])
                            errors = True
                            return (None)
                        if not has_numbers(str(dimensions['dim'][r]['value'])):
                            if dimensions['dim'][r]['value'] not in sym_dct.keys():
                                print('\t-Most likely this [%s] should be a symbol but has not been entered in the definition as one' % dimensions['dim'][r]['value'])
                                val = 1
                                sym_dct[dimensions['dim'][r]['value']] = val

                            else:
                                #substitute the value for the one defined for the symbol
                                val = int(sym_dct[dimensions['dim'][r]['value']])
                        else:
                            val = int(dimensions['dim'][r]['value'])

                        arr.append(val)
                        use_dims = True
                else:
                    arr.append(1)
            if use_dims:
                if(nx_type.find('NX_INT') > -1):
                    data = np.ones(tuple(arr), dtype=np.int)
                elif(nx_type.find('NX_NUMBER') > -1):
                    data = np.ones(tuple(arr), dtype=np.int)
                elif(nx_type.find('NX_FLOAT') > -1):
                    data = np.ones(tuple(arr), dtype=np.float)
                elif (nx_type.find('NX_CHAR') > -1):
                    data = np.chararray(tuple(arr))
                    data[:] = '!some char data!'


    if(nx_type.find('NX_CHAR') > -1):
        if(data is None):
            return('!some char data!')
        else:
            return(data)
    elif(nx_type.find('NX_FLOAT') > -1):
        if (use_dims):
            return(data)
        else:
            return(1.0)
    elif (nx_type.find('NX_INT') > -1):
        if (use_dims):
            return (data)
        else:
            return (1)
    elif (nx_type.find('NX_BOOLEAN') > -1):
        #return False, NX_BOOLEAN's are int8's
        return (np.int8(0))

    elif (nx_type.find('NX_DATE_TIME') > -1):
        return(make_timestamp_now())
    elif (nx_type.find('NX_NUMBER') > -1):
        if (use_dims):
            return (data)
        else:
            return (1.0)
    elif (nx_type.find('NX_POSINT') > -1):
        if (use_dims):
            return (data)
        else:
            return (1)
    elif (nx_type.find('NX_UINT') > -1):
        if (use_dims):
            return (data)
        else:
            return (1)

def make_timestamp_now():
    """
    create a ISO 8601 formatted time string for the current time and return it
    """
    t = datetime.datetime.now().isoformat()
    return (t)

def get_entry(nf):
    '''
    return the name of the entry in the file
    '''
    keys = list(nf.keys())
    s1 = 'entry'
    for k in keys:
        if s1.casefold() == k.casefold():
            return(nf[k], k)
        else:
            pass
    return(nf[k], s1)

def get_NXdata_nm(nf):
    '''
    find the first NXdata group and return its name
    '''
    entry_grp, entry_nm = get_entry(nf)
    keys = list(entry_grp.keys())
    s1 = 'NXdata'
    for k in keys:
        if s1.casefold() == entry_grp[k].attrs['NX_class'].casefold():
            return(entry_grp[k], k)
    return(None, None)

def get_all_paths_in_hdf5(nf):
    list(nf.keys())
    list(nf.values())
    members = []
    nf.visit(members.append)
    return(members)

def get_NXdataset_nm(nxdata_grp):
    keys = list(nxdata_grp.keys())
    #remove the most likely keys that we do not want for sure
    keys = trim_dset_list(keys)
    res = None
    for k in keys:
        if(k.casefold() == 'data'):
            return(k)
    if(len(keys) > 0):
        #just return the first one for now
        return(keys[0])
    else:
        return(None)

def trim_dset_list(dset_lst):
    rem_lst = ['energy', 'sample_x', 'sample_y']
    lst = []
    for d in dset_lst:
        if(d.casefold() not in rem_lst):
            lst.append(d)
    return(lst)

def has_numbers(inputString):
    #make sure it is a string
    inputString = str(inputString)
    return all([c.isdigit() or c == '.' for c in inputString])

def get_symbols(fname):
    '''# print(root.xpath("//article[@type='news']/content/text()"))
    # print(root.xpath("//article"))
    '''
    from bs4 import BeautifulSoup
    infile = open(fname, "r")
    contents = infile.read()
    infile.close()
    soup = BeautifulSoup(contents, 'xml')
    symbols = soup.find_all('symbol')
    slst = []
    for symbol in symbols:
        #print(symbol)
        slst.append({'name': symbol.get('name'), 'doc': symbol.get_text(), 'value': 1})

    return(slst)

def process_symbols(soup, sym_args_dct={}):
    '''
    this function pulls the symbols if any are defined and then substitutes those symbols for ones defined by the user
    in usr_args (if the user passed them in on the command line), if no user args define values for each symbol the
    symbol will be assigned the default value of 1
    '''
    symbols = soup.find_all('symbol')
    slst = []
    sym_dct = {}
    for symbol in symbols:
        sym_nm = symbol.get('name')
        val = 1
        doc = symbol.get_text()
        #print(symbol)
        if(sym_nm in sym_args_dct.keys()):
            #use the user passed in value for this symbol
            val = sym_args_dct[sym_nm]
            print('\tsymbol [%s] will use the value [%s] passed in by user' % (sym_nm, str(val)))
        else:
            if(sym_nm == 'dataRank'):
                print('\tsymbol [%s] was not defined and passed in in the usr_args, so it will be auto calculated at every occurance' % (sym_nm))
            else:
                print('\tsymbol [%s] was not defined and passed in in the usr_args, so using default value of 1 for [%s]' % (sym_nm,sym_nm))

        if(type(val) is dict):
            #if users passed in symbols from the command line these will  be in a dict
            val = val['value']
        
        slst.append({'name': sym_nm, 'doc': doc, 'value': val})
        sym_dct[sym_nm] = {'doc': doc, 'value': val}

    #now walk through each dimension definition and perform symbol substitutions to the read in xml doc where applicable
    # get all dimensions fields where rank is defined using keyword 'dataRank'
    # drank_tags_lst = soup.select('[rank^="dataRank"]')
    drank_tags_lst = soup.find_all('dimensions')
    for dimns in drank_tags_lst:
        max_index = 1
        #first check attrs of this dimensions field for symbols used for values
        cntnts = dimns.contents
        for cntnt_attr in cntnts:
            if(not type(cntnt_attr) == bs4.element.Tag):
                continue
            if 'value' in cntnt_attr.attrs.keys():
                if (cntnt_attr.attrs['value'] in sym_dct.keys()):
                    cntnt_attr.attrs['value'] = sym_dct[ cntnt_attr.attrs['value'] ]['value']

        if 'rank' in dimns.attrs.keys():
            dim_lst = dimns.find_all('dim')
            for d in dim_lst:
                reqd = True
                #d is a dimensions dict
                idx = int(d['index'])

                if('value' not in d.attrs.keys()):
                    print('\t\tError, there is no [value] key in dim specification', d.attrs)
                    continue
                if(d.attrs['value'] in sym_dct.keys()):
                    # # dimension is required if not specified or if set to true (will it ever be explicitly?)
                    # the definition specifies a symbol as the value for this dimension so substitute it
                    d.attrs['value'] = sym_dct[ d.attrs['value'] ]['value']
                # dimension is required if not specified or if set to true (will it ever be explicitly?)
                if 'required' in d.attrs.keys():
                    if d.attrs['required'] == 'false':
                        reqd = False
                #record max_index so we can set 'dataRank' if it is used
                if reqd and (idx > max_index):
                    max_index = idx

            #now (if it is specified) substitute max_index for 'dataRank' keyword
            if('rank' in dimns.attrs.keys()):
                if dimns.attrs['rank'] == 'dataRank':
                    dimns.attrs['rank'] = str(max_index)

    # all symbol substitutions have been made in the 'soup'
    xml = soup.prettify(encoding='utf-8')
    xml = xml.decode('utf-8')
    return(xml, sym_dct)


def get_xml_paths(fname, sym_args_dct={}, report_symbols_only=False):
    '''
    takes the path to teh nxdl.xml file and returns a dict of element category lists of the entire structure
    '''
    if(not os.path.exists(fname)):
        print('XML file [%s] does not exist' % fname)
        return

    infile = open(fname, "r")
    contents = infile.read()
    infile.close()
    contents = contents.replace('xmlns="http://definition.nexusformat.org/nxdl/3.1"','')
    contents = contents.replace('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n', '')
    contents = contents.replace('xsi:schemaLocation="http://definition.nexusformat.org/nxdl/3.1 ../nxdl.xsd"', '')
    soup = bs4.BeautifulSoup(contents, 'xml')
    # syms = get_symbols(fname)
    xml, syms = process_symbols(soup, sym_args_dct=sym_args_dct)
    if(report_symbols_only):
        exit(0)

    ldct = {}
    dct = {}
    xml = xml.replace('encoding="utf-8"', '')

    xxml = etree.XML(xml)
    #xxml = etree.parse(fname).getroot()
    tree = etree.ElementTree(xxml)
    root = tree.getroot()

    def_dir = root.get('category')
    dct['category'] = def_dir
    dct['doc'] = ''
    ch = root.getchildren()

    #confirm that an NXentry group exists, if not then bail
    entry = soup.find(type='NXentry')
    if(not entry):
        return(None, None)

    for c in ch:
        if(c.tag == 'doc'):
            dct['doc'] = c.text
        elif(c.tag == 'group'):
            entry_grp = c
            break

    skip_lst = ['doc']
    ch_lst = get_children(entry_grp)
    if (len(ch_lst) > 0):
        for ch_dct in ch_lst:
            if ch_dct['ptype'] not in skip_lst:
                hsh = hash(ch_dct['xpath'])
                #print(ch_dct)
                if hsh not in ldct.keys():
                    #print(ch_dct['ptype'] + ch_dct['abspath'])
                    if ch_dct['ptype'] not in dct.keys():
                        dct[ch_dct['ptype']] = []

                    dct[ch_dct['ptype']].append(
                        {'abspath': ch_dct['abspath'], 'xpath': ch_dct['xpath'], 'attrib': dict(ch_dct['attrib']),
                         'doc': ch_dct['doc']})
                    ldct[hsh] = 1

    #pprint.pprint(dct)
    return (dct, syms)

def get_parent_group(nf, ppath):

    if (ppath == ''):
        pgrp = nf
    else:
        if ppath not in nf:
            print('\t\tError: why doesnt [%s] exist?' % ppath)
        else:
            pgrp = nf[ppath]
    return(pgrp)

def get_enums(abspath, dct):
    '''
    for a given parent path, return all enumerations as a list
    '''
    l = []
    for d in dct['item']:
        if(abspath == d['abspath']):
            l.append(d['attrib']['value'])
    return(l)

def fix_nx_name(nm):
    '''
    it appers to be default that if no name attribute was passed then the NX class name is used in upper case sans 'NX'
    '''
    # if nm.find('NX') > -1:
    #     #remove NX and make it upper case
    #     nm = nm.replace('NX','').upper()
    #     #nm = nm.replace('NX', '').lower()
    return(nm)

def fix_nx_path(path_str):
    p2 = path_str.split('/')
    s = '/'
    for ss in p2:
        if(len(ss) > 0):
            s += fix_nx_name(ss) + '/'
    return(s)


def create_groups(nf, dct):
    '''
    walk all dicts of type GROUP creating them as it goes
    '''
    for d in dct['group']:
        _type = get_type(d)
        if('name' in d['attrib'].keys()):
            if _type.replace('NX','') == d['attrib']['name']:
                #use the _type as the name
                #name = _type
                name = d['attrib']['name']
            else:
                name = fix_nx_name(d['attrib']['name'])
        else:
            name = fix_nx_name(_type)

        ppath = fix_nx_path(get_parent_path(d['abspath']))
        if (ppath == ''):
            pgrp = nf
        else:
            pgrp = nf[ppath]
        min_occurs_str = get_min_occurs(d, dct['category'])
        _grp = _group(pgrp, name, nxdata_type=_type)
        _string_attr(_grp, 'required', min_occurs_str)
        doc = get_doc(d)
        if (doc):
            _string_attr(_grp, 'doc', doc)
        #print('created: GROUP [%s]' % fix_nx_path(d['abspath']))

def get_dimensions_dicts(d, dct):
    dimensions_dct = next((item for item in dct['dimensions'] if item["abspath"] == d['abspath']), {'attrib':{}})
    #dim_dct = next((item for item in dct['DIM'] if item["abspath"] == d['abspath']), {'attrib':{}})
    dim_l = []
    if('dim' in dct.keys()):
        for item in dct['dim']:
            #get all who share the abspath
            if item['abspath'] == d['abspath']:
                dim_l.append(item['attrib'])

    dimensions_dct['attrib']['dim'] = dim_l
    #dimensions_dct['attrib'].update(dim_dct['attrib'])
    return(dimensions_dct)

def create_fields(nf, dct, sym_dct={}, category=''):
    '''
        walk all dicts of type FIELD creating them as it goes

        {'abspath': '/entry/NXinstrument/fluorescence/data/',
          'xpath': '/definition/group/group[1]/group[3]/field[1]',
          'attrib': {'axes': 'energy',
           'name': 'data',
           'signal': '1',
           'type': 'NX_INT'},
          'doc': '\n     '},
    '''
    valid_fld_attr_nms_lst = ['axes','axis','data_offset','interpretation','long_name','maxOccurs','minOccurs','nameType','primary','signal','stride','units'] #type was removed because I think it is handled when dataset is created
    # create FIELDs
    for d in dct['field']:
        name = fix_nx_name(d['attrib']['name'])
        _type = get_type(d)

        #get teh parent path to this field
        ppath = fix_nx_path(get_parent_path(d['abspath']))

        #get all enumerations if any exist for this parent path
        enums = get_enums(d['abspath'], dct)
        #get the dimensions dict if one exists for this field
        if('dimensions' in dct.keys()):
            use_dim_dct_lst = get_dimensions_dicts(d, dct)
        else:
            use_dim_dct_lst = {}
        pgrp = get_parent_group(nf, ppath)
        if len(enums) > 0:
            #if this is an enumerated data type just use teh first enumeration as the data
            data = enums[0]
        else:
            data = get_nx_data_by_type(_type, use_dim_dct_lst, sym_dct)
            if(data is None):
                print('\t\tError: There is an issue with a non standard field for fieldname [%s]' % name)
                return(False)
        _dset = _dataset(pgrp, name, data, _type)
        #print('created: FIELD [%s]' % fix_nx_path(d['abspath']))
        _string_attr(_dset, 'required', get_min_occurs(d, category))
        doc = get_doc(d)
        if (doc):
            _string_attr(_dset, 'doc', doc)

        # check for other attributes
        skip_lst = ['minOccurs', 'maxOccurs']
        for a_nm in valid_fld_attr_nms_lst:
            if(a_nm in skip_lst):
                continue
            if a_nm in d['attrib'].keys():
                #check if it already exists
                if a_nm in _dset.attrs.keys():
                    #reassign its value
                    _dset.attrs[a_nm] = d['attrib'][a_nm]
                else:
                    #create it
                    _string_attr(_dset, a_nm, d['attrib'][a_nm])

    return(True)

def create_links(nf, dct):
    '''
    walk all dicts of type LINK creating them as it goes

    '''
    if('link' not in dct.keys()):
        return
    paths_lst = get_all_paths_in_hdf5(nf)
    for d in dct['link']:
        fix_link_target(nf, d, paths_lst)

def fix_link_target(nf, trgt_dct, hdf5_path_lst):
    '''
    pull the actual paths from hdf5 file and make sure the link uses same case sensitivity

    source_addr = u"/entry/instrument/detector/two_theta"   # existing data
    target_addr = u"two_theta"                              # new location
    ds_tth.attrs[u"target"] = source_addr                   # a NeXus API convention for links
    nxdata[target_addr] = f[source_addr]                    # hard link
    # nxdata._id.link(source_addr, target_addr, h5py.h5g.LINK_HARD)

    '''
    ppath = get_parent_path(trgt_dct['abspath'])
    if ppath not in nf:
        print('\t-Error: while checking the links, this parent path [%s] not exist in generated file' % ppath)
        print('\t\ttarget path: [%s] ' % trgt_dct['abspath'])
        exit()
    else:
        pgrp = nf[ppath]
        target_str = trgt_dct['attrib']['target']

        #check target link path against all valid paths in nf file
        for p in hdf5_path_lst:
            # irespective of case is this path a match?
            pstr = '/' + p
            if pstr.casefold() == target_str.casefold():
                # yep  so make sure it uses the valid path case sensitivity
                target_str = p
                break

        if target_str[0] != '/':
            target_str = '/' + target_str

        link_nm = get_last_name_in_path(trgt_dct['abspath'])
        if(target_str not in nf):
            #print('\t-Error: The link path [%s] specified in NXDL file for [%s] does not exist in the generated file' % (target_str, trgt_dct['abspath']))
            print('\t-Link Error: This field [%s] specifies a link target that does not exist in the generated file [%s]' % (trgt_dct['abspath'], target_str))
            #exit()
        else:
            pgrp[link_nm] = nf[target_str]
            nf[target_str].attrs['target'] = target_str


def create_attributes(nf, dct):
    '''
    '''

    if('attribute' not in dct.keys()):
        return
    paths_lst = get_all_paths_in_hdf5(nf)
    for d in dct['attribute']:
        #print(d)
        ppath = get_parent_path(d['abspath'])
        if ppath not in nf:
            print('\t-Error: while creating Attributes, this parent path [%s] not exist in generated file' % ppath)
            exit()
        else:
            pgrp = nf[ppath]

        if('type' in d['attrib'].keys()):
            data = get_nx_data_by_type(d['attrib']['type'])
        else:
            data = get_nx_data_by_type('NX_CHAR')

        pgrp.attrs[d['attrib']['name']] = data
        #_string_attr(pgrp, d['attrib']['name'], data)

def get_last_name_in_path(pth):
    p2 = pth.split('/')
    for p in p2:
        if(len(p) == 0):
            p2.remove(p)
    nm = p2[-1]
    return(nm)


def make_class_as_nf_file(clss_nm, path_dct, dest_dir, symbol_dct = {}):
    print('\texporting: [%s]' % clss_nm)
    res = True
    category = def_dir = path_dct[clss_nm]['category']

    if (not os.path.exists(dest_dir)):
        os.makedirs(dest_dir)

    fpath = os.path.join(dest_dir, '%s.hdf5' % clss_nm)
    nf = h5py.File(fpath, 'w')

    sym_dct = {}
    # process SYMBOLS
    for sym_nm, d in symbol_dct.items():
        if (True):
            #sym_nm = d['name']
            val = int(d['value'])
        else:
            #sym_nm = d['name']
            val = default_symbol_val

        sym_dct[sym_nm] = val

        #create the symbol string attrs in the root of the file
        _string_attr(nf, sym_nm, d['doc'])

        # update the DIMENSIONS list by substituting the value for the symbol where it is used to specify the dimension of
        # a field
        if('dimensions' in path_dct[clss_nm].keys()):
            for l in path_dct[clss_nm]['dimensions']:
                if 'rank' in l['attrib'].keys():
                    if l['attrib']['rank'] == sym_nm:
                        #substitute the value
                        l['attrib']['rank'] = val

        if ('dim' in path_dct[clss_nm].keys()):
            for l in path_dct[clss_nm]['dim']:
                if 'value' in l['attrib'].keys():
                    if l['attrib']['value'] == sym_nm:
                        #substitute the value
                        l['attrib']['value'] = val

    #check if the definition uses a symbol for a value but has not defined that same symbol
    if('dim' in path_dct[clss_nm].keys()):
        for l in path_dct[clss_nm]['dim']:
            if 'value' in l['attrib'].keys():
                val = l['attrib']['value']
                if not has_numbers(val):
                    #does it also contain spaces? if so then it is not a symbol
                    if val.find(' ') == -1:
                        if val not in sym_dct.keys():
                            print('\t-Symbol Warning: the symbol [%s] is being used but has not been defined in the Symbols table, setting to default value of 1' % val)
                            sym_dct[val] = 1
                            l['attrib']['value'] = 1


    # create GROUPs
    create_groups(nf, path_dct[clss_nm])
    # # create FIELDs
    res = create_fields(nf, path_dct[clss_nm], sym_dct, category)

    # create Links
    create_links(nf, path_dct[clss_nm])

    if(res):
        # create Attributes
        create_attributes(nf, path_dct[clss_nm])

        _string_attr(nf, 'file_name', fpath)
        _string_attr(nf, 'file_time', make_timestamp_now())
        entry_grp, entry_nm = get_entry(nf)
        #ensure the definition is correct
        entry_grp['definition'][()] = clss_nm
        _string_attr(nf, 'default', entry_nm)
        nx_data_grp, nx_data_nm = get_NXdata_nm(nf)
        if (nx_data_nm):
            _string_attr(entry_grp, 'default', nx_data_nm)
            dset_nm = get_NXdataset_nm(nx_data_grp)
            if (dset_nm):
                _string_attr(nx_data_grp, 'signal', dset_nm)
                _string_attr(nx_data_grp[dset_nm], 'signal', '1')

        nf.close()
        print('finished exporting to [%s]' % fpath)
    else:
        print('Failed exporting [%s]' % fpath)
        nf.close()
    return(res)



def build_class_dict(class_dir='base_classes', desired_class=None, defdir=None, sym_args_dct={},report_symbols_only=False):
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
        class_nm = nxdl_file.replace('.nxdl.xml', '')
        if(class_nm.find(os.path.sep) > -1):
            class_nm = class_nm.split(os.path.sep)[-1]
        print('\nProcessing [%s]' % nxdl_file)
        resp_dict, syms = get_xml_paths(nxdl_file, sym_args_dct=sym_args_dct, report_symbols_only=report_symbols_only)
        dct[class_nm] = resp_dict
    return(dct, syms)

def symbol_args_to_dict(arg_lst):
    dct = {}
    for arg in arg_lst:
        k,v = arg.replace(',','').strip().split('=')
        dct[k] = {'value': v, 'doc': ''}

    return(dct)

if __name__ == '__main__':
    import argparse

    def_subdirs = ['applications', 'contributed_definitions']

    parser = argparse.ArgumentParser(description="This is a script to generate hdf5 files from nxdl.xml definitions")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-f","--file",
                        help="The definition file to generate.\nex: python nxdl_to_hdf5.py --f NXstxm")
    group.add_argument("-d","--directory",
                        help="generate all definitions in this directory one of either ['applications', 'contributed_definitions'], ex: applications")
    parser.add_argument("-s","--symbols",
                        help="pass comma delimited set of key value pairs for each desired symbol \nex: python nxdl_to_hdf5.py --f NXstxm --s numP=24, numE=1, numY=10, numX=10", nargs='*')
    parser.add_argument("--nxdefdir", help="Specify an alternative location to the NXDL definitions base directory (where nexpy is installed)")
    parser.add_argument("-r", "--report", help="Report on the Symbols that this definition uses", action="store_true")

    args = parser.parse_args()
    sym_args_dct = {}
    class_nm = None
    class_path = None
    report_symbols_only = False
    if args.file:
        print('\tProcess this specific definition [%s]' % args.file)
        class_nm = args.file
    elif args.directory:
        print('\tProcess this entire directory [%s]' % args.directory)
        def_subdirs = [args.directory]
    else:
        print('\tError: neither a specific definition or directory was specified so nothing to do')
        exit()

    if args.symbols:
        print('\tProcess using the following symbols [%s]' % args.symbols)
        sym_args_dct = symbol_args_to_dict(args.symbols)

    if args.nxdefdir:
        print('\tUsing the following definitions base directory [%s]' % args.nxdefdir)
        def_dir = args.nxdefdir
    else:
        #use the definitions in the installed nexpy
        def_dir = os.path.join(os.path.dirname(__file__), '..','definitions')

    if args.report:
        #just repolrt on the symbols that are defined in
        #only perform a symbol report if the user specified a file
        if(class_nm):
            report_symbols_only = True

    #only search in applications and contributed_definitions subdirectories
    if(class_nm):
        for def_subdir in def_subdirs:
            class_path = os.path.join(def_dir, def_subdir, class_nm + '.nxdl.xml')
            if(os.path.exists(class_path)):
                break
            else:
                class_path = None

        if(class_path is None):
            print('Error: the class name [%s.nxdl.xml] doesnt exist in either of the applications or contributed_definitions subdirectories' % class_nm)
            exit()

    files = None
    for def_subdir in def_subdirs:
        files = sorted(os.listdir(os.path.join(def_dir, def_subdir)))
        dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nxdl', def_subdir)
        dest_dir = r'G:\tst_nexus\exampledata\nxdl\applications'
        for class_path in files:
            if class_path.find('.nxdl.xml') > -1:
                if(class_nm is None):
                    class_nm = class_path.replace('.nxdl.xml','')
                    path_dct, syms  = build_class_dict(def_subdir, desired_class=class_nm, defdir=def_dir,
                                                       sym_args_dct=sym_args_dct,
                                                       report_symbols_only=report_symbols_only)
                    if(path_dct[class_nm] is None):
                        print('\t[%s] does not contain an NXentry group, skipping' % class_nm)
                        class_nm = None
                        continue

                    res = make_class_as_nf_file(class_nm, path_dct, dest_dir, symbol_dct=sym_args_dct)
                    # if(res):
                    #     run_remote_validator(class_nm)
                    # else:
                    #     print('Not validating the file until NXDL file contains no errors')
                    class_nm = None
                else:
                    path_dct, syms = build_class_dict(def_subdir, desired_class=class_nm,
                                                      defdir=def_dir, sym_args_dct=sym_args_dct,
                                                      report_symbols_only=report_symbols_only)
                    if (path_dct[class_nm] is None):
                        print('\t[%s] does not contain an NXentry group, skipping' % class_nm)
                        class_nm = None
                        continue

                    res = make_class_as_nf_file(class_nm, path_dct, dest_dir, symbol_dct=sym_args_dct)
                    # if (res):
                    #     run_remote_validator(class_nm)
                    # else:
                    #     print('Skipping file validation until [%s] contains no errors' % os.path.join(os.path.join(def_dir, def_subdir), class_nm +'nxdl.xml'))
                    exit()



