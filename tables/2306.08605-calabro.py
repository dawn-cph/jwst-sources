"""
Parse table from Calabro et al. 2023

https://github.com/Anthony96/Line_measurements_nearIR

"""

from grizli import utils
raw = utils.read_catalog('https://raw.githubusercontent.com/Anthony96/Line_measurements_nearIR/main/public_release_line_meas_Calabro23_v1.txt')

for c in list(raw.colnames):
    raw.rename_column(c, c.lower())
    
raw['zspec'] = raw['hb_z']
raw['id','ra','dec','zspec'].write('2306.08605-calabro.csv', overwrite=True)

print('2306.08605-calabro.csv')

