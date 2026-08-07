from grizli import utils, catalog
from astropy.coordinates import SkyCoord
import numpy as np

raw = utils.read_catalog("2508.21229-matsuoka.txt")

coo_str = [
    '{rh:02d}:{rm:02d}:{rs:.2f} {dd:02d}:{dm:02d}:{ds:.2f}'.format(**row)
    for row in raw
]
coo = SkyCoord(coo_str, unit=('hour','degree'))

tab = utils.GTable()
id_str = 'shellqs-{Paper}_j{rh:02d}{rm:02d}{rs:.2f}--{dd:02d}{dm:02d}{ds:.1f}'

src_id = [
    id_str.format(**row).replace('---','m').replace('--','p')
    for row in raw
]

tab['id'] = src_id
tab['ra'] = coo.ra.deg
tab['dec'] = coo.dec.deg
tab['type'] = raw['ID']
tab['z/SpT'] = raw['z/SpT']

tab['z_spec'] = -1.0
has_z = ~np.isin(tab['type'], ['BD','P'])
tab['z_spec'][has_z] = raw['z/SpT'][has_z].astype(float)

tab['ra'].format ='.6f'
tab['dec'].format = '.6f'
tab['z_spec'].format = '.3f'

tab.write('2508.21229-matsuoka.csv', overwrite=True)