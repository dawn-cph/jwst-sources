
from grizli import utils
import astropy.table

# From https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/A%2bA/654/A80/tableb1
from grizli import utils, catalog
import astropy.table

viz_cdfs = catalog.query_tap_catalog(
    ra=None,
    db=f'"J/A+A/647/A150/cdfs"',
    vizier=True, max=20000
)

viz_uds = catalog.query_tap_catalog(
    ra=None,
    db=f'"J/A+A/647/A150/uds"',
    vizier=True, max=20000
)

viz = astropy.table.vstack([viz_cdfs, viz_uds])

viz['id'] = [n for n in viz['Name']]
viz['ra'] = viz['RAJ2000']
viz['dec'] = viz['DEJ2000']
viz['zspec'] = viz['zsp']
viz['ra'].format = '.6f'
viz['dec'].format = '.6f'
viz['id','ra','dec','zspec','q_zsp'].write('2101.07645-garilli.csv', overwrite=True)
