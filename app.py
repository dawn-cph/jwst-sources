import os
import glob

import numpy as np
from flask import Flask, request, send_file
from grizli import utils

import json

from parse_coords import parse_coords

app = Flask(__name__)
app.debug = True

def get_hashroot():
    rnd = int(np.random.rand()*100000)
    return f'{rnd:05d}'


@app.route("/")
def show_table():
    """
    Dump jwst-sources.html
    """
    with open('jwst-sources.html') as fp:
        lines = fp.readlines()
    return ''.join(lines)


#
@app.route("/help")
def show_help():
    """
    Dump jwst-sources.html
    """
    with open('help.html') as fp:
        lines = fp.readlines()
    return ''.join(lines)


@app.route("/jname")
def make_jname():
    """
    matches close to a position
    """
    kwargs = dict(ra=214.914500, dec=52.94304, sep=1)

    for k in kwargs:
        if request.args.get(k) is not None:
            #kwargs[k] = request.args[k]
            if request.args[k].lower() in ['false','true']:
                kwargs[k] = request.args[k].lower() == 'true'
            else:
                kwargs[k] = float(request.args[k])
                 
    coo = request.args.get('coords')
    if coo is not None:
        kwargs['ra'], kwargs['dec'] = parse_coords(coo)
    
    src = utils.read_catalog('jwst-sources.csv')
    
    this = utils.GTable()
    this['ra'] = [kwargs['ra']]
    this['dec'] = kwargs['dec']
    
    idx, dr = this.match_to_catalog_sky(src)
    hasm = dr.value < kwargs['sep']
    
    if hasm.sum() > 0:
        jname = src['jname'][hasm][0]
    else:
        jname = utils.radec_to_targname(kwargs['ra'], kwargs['dec'],
                                round_arcsec=(0.00001, 0.00001), 
                                precision=2,
                targstr='j{rah}{ram}{ras}.{rass}{sign}{ded}{dem}{des}.{dess}')
    
    res = {'jname':jname, 'nmatch':int(hasm.sum()),
           'ra':kwargs['ra'], 'dec':kwargs['dec']}
                               
    return json.dumps(res)


@app.route("/match")
def nearest_matches():
    """
    matches close to a position
    """
    kwargs = dict(ra=214.914500, dec=52.94304, sep=1)

    for k in kwargs:
        if request.args.get(k) is not None:
            #kwargs[k] = request.args[k]
            if request.args[k].lower() in ['false','true']:
                kwargs[k] = request.args[k].lower() == 'true'
            else:
                kwargs[k] = float(request.args[k])
                 
    coo = request.args.get('coords')
    if coo is not None:
        kwargs['ra'], kwargs['dec'] = parse_coords(coo)
    
    src = utils.read_catalog('jwst-sources.csv')
    
    this = utils.GTable()
    this['ra'] = [kwargs['ra']]
    this['dec'] = kwargs['dec']
    
    idx, dr = this.match_to_catalog_sky(src)
    hasm = dr.value < kwargs['sep']
    
    if hasm.sum() == 0:
        return 'No sources found within {sep:.1}" of {ra:.6f},{dec:.5f}'.format(**kwargs)
    
    src['dr'] = dr.value
    src = src[hasm]
    src['dr'].format= '.2f'
    src['dr'].description = 'Offset from {ra:.6f}, {dec:.5f} in arcsec'.format(**kwargs)
    
    sub = src['jname','count','F200W','F444W','ra','dec','dr','zphot','zspec','arxiv','author']
    out = 'tmp'+get_hashroot()
    
    sub.write_sortable_html(out, 
                            localhost=False, max_lines=100000, 
                            filter_columns=['count','ra','dec',
                                            'dr','zphot','zspec'])
    
    with open(out) as fp:
        lines = fp.readlines()
    
    os.remove(out)
    
    return ''.join(lines)
    
    