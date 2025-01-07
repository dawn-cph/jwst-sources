from grizli import utils

# From https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/A%2bA/654/A80/tableb1
from grizli import utils, catalog
import astropy.table

viz = catalog.query_tap_catalog(
    ra=None,
    db=f'"J/A+A/654/A80/tableb1"',
    vizier=True, max=20000
)

viz['id'] = viz['ID']
viz['ra'] = viz['RAJ2000']
viz['dec'] = viz['DEJ2000']
viz['zspec'] = viz['z']


viz['id','ra','dec','zspec','Conf'].write('2108.01713-schmidt.csv', overwrite=True)