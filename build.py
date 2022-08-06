import yaml
import glob
import os

import numpy as np
from astropy.coordinates import SkyCoord
import astropy.table

from grizli import utils

## Read tables

files = glob.glob('tables/*csv')
files.sort()

tabs = []
ids = []

for file in files:
    meta = file.replace('.csv','.meta')
    if not os.path.exists(meta):
        print(f'meta file {meta} not found for {file}')
        continue
    
    print(f'Read table: {file}')
    try:
        tab = utils.read_catalog(file)
    except:
        print(f'Failed to read table: {file}')
        continue
    
    with open(meta) as fp:
        try:
            _meta = yaml.load(fp, Loader=yaml.SafeLoader)
        except:
            print(f'ERROR: Failed to parse {meta}, check that there are no ":" or incompatible linebreaks in `description`')
            continue
    
    meta_ok = True
    for k in ['arxiv','author']:
        if k not in _meta:
            print(f'ERROR: `{k}` keyword not found in {meta}')
            meta_ok = False
    
    if not meta_ok:
        continue
        
    for k in ['arxiv','author']:
        tab[k] = _meta[k]
    
    if 'rah' in tab.colnames:
        try:
            coo = SkyCoord(tab['rah'], tab['decd'], unit=('hour','deg'))
        except:
            print(f'Failed to parse rah/decd coordinates in  {file}')
            continue
            
        tab['ra'] = coo.ra.deg
        tab['dec'] = coo.dec.deg
    
    #tab['id'] = 
    ids.extend([f'{_id}' for _id in tab['id']])
    tab.remove_column('id')
    
    tab['jname'] = [utils.radec_to_targname(ra, dec,
                                round_arcsec=(0.00001, 0.00001), 
                                precision=2,
                    targstr='j{rah}{ram}{ras}.{rass}{sign}{ded}{dem}{des}.{dess}')
                     for ra, dec in zip(tab['ra'], tab['dec'])]
    
    if len(tabs) > 0:
        # If matches exist in files already processed, get the 
        # jname from there
        _full = utils.GTable(astropy.table.vstack(tabs))
        idx, dr = _full.match_to_catalog_sky(tab)
        hasm = dr.value < 0.5
        
        if hasm.sum() > 0:
            tab['jname'][hasm] = _full['jname'][idx][hasm]
        
    tabs.append(tab)

# Concatenated table

full = utils.GTable(astropy.table.vstack(tabs))
full['id'] = ids

jn = utils.Unique(full['jname'], verbose=False)
full['count'] = 1
for name, ct in zip(jn.values, jn.counts):
    full['count'][jn[name]] = ct
                   
so = np.argsort(full['jname'])      
full = full[so]
full['ra'].format = '.6f'
full['ra'].description = 'Right Ascension, deg'

full['dec'].format = '.5f'
full['dec'].description = 'Declination, deg'

full['zphot'].format = '.2f'
full['zphot'].description = 'Photometric redshift'

if 'zspec' not in full.colnames:
    full['zspec'] = -1.0
    
full['zspec'].format = '.3f'
full['zspec'].description = 'Spectroscopic redshift'

full['count'].description = 'Number of references'

thumb = '<img src="http://grizli-cutout.herokuapp.com/thumb?ra={ra}8&dec={dec}&filters={filt}&size=1&scl={scl}&invert=True" height=100px />'
full['F200W'] = [thumb.format(filt='f200w-clear', scl=16, **row) for row in full]
full['F444W'] = [thumb.format(filt='f444w-clear', scl=24, **row) for row in full]

full.write('jwst-sources.csv', overwrite=True)

sub = full['jname','count','F200W','F444W','ra','dec','zphot','zspec','arxiv','author']
sub.write_sortable_html('jwst-sources.html', 
                        localhost=False, max_lines=100000, 
                        filter_columns=['count','ra','dec','zphot','zspec'])
                        

