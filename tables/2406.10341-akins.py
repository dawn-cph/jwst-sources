from grizli import utils
tab = utils.read_catalog("https://raw.githubusercontent.com/hollisakins/akins24_cw/refs/heads/main/COSMOS-Web_LRDs.dat", format='ascii.ecsv')

tab['zphot'] = tab['z_gal_med']
tab['id','ra','dec','zphot'].write('2406.10341-akins.csv')
