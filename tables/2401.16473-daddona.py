from grizli import utils, catalog
import astropy.table

viz = catalog.query_tap_catalog(
    ra=None,
    db=f'"J/A+A/686/A4/tablee1"',
    vizier=True, max=20000
)

for c in viz.colnames:
    viz.rename_column(c, c.lower())

viz['ra'] = viz['raicrs']
viz['dec'] = viz['deicrs']

viz['id','ra','dec','zspec','source', 'qf'].write(
    '2401.16473-daddona.csv', overwrite=True
)