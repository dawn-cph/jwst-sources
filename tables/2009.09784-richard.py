from grizli import utils, catalog
import astropy.table

clusters = """
a2744
a370
mc257
mc329
mc416ne
mc416s
bullet
mc940
mc1206
rxj1347
smc2031
smc2131
mc2214
""".split()

viz = []
for cluster in clusters:
    _viz = catalog.query_tap_catalog(
        ra=None,
        db=f'"J/A+A/646/A83/{cluster}"',
        vizier=True, max=20000
    )
    _viz['cluster'] = cluster
    viz.append(_viz)

viz = astropy.table.vstack(viz)

viz['id'] = ["{cluster}-{Iden}".format(**row) for row in viz]
viz['ra'] = viz['RAJ2000']
viz['dec'] = viz['DEJ2000']
viz['zspec'] = viz['z']

viz['id','ra','dec','zspec','zconf'].write('2009.09784-richard.csv', overwrite=True)