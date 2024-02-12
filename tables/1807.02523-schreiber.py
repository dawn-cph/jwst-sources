from grizli import utils

# From https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/A+A/618/A85
viz = utils.read_catalog('1807.02523-schreiber.vot', format='votable')

viz['id'] = viz['ID']
viz['ra'] = viz['RAJ2000']
viz['dec'] = viz['DEJ2000']
viz['zspec'] = viz['zs']

viz['id','ra','dec','zspec'].write('1807.02523-schreiber.csv', overwrite=True)
