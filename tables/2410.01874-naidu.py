import astropy.table

from grizli import utils
alt = utils.read_catalog("https://zenodo.org/records/13871850/files/ALT_DR1_public.fits")

# zspec = z_ALT where n_lines_detected > 1
alt['zspec'] = astropy.table.MaskedColumn(
    name='zspec',
    data=alt['z_ALT'],
    mask=(alt['n_lines_detected'] == 1),
)

alt.write('2410.01874-naidu.csv', overwrite=True)