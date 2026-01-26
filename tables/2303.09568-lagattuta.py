from grizli import utils

# https://academic.oup.com/mnras/article/522/1/1091/7081353
# rxj0437_redshift_catalogue_supplement.fits from supplementary data

muse = utils.read_catalog("2303.09568-lagattuta-suppl.fits.gz", format="fits")

for c in list(muse.colnames):
    muse.rename_column(c, c.lower())

muse.rename_column('id', 'orig_id')
muse['id'] = [
    '_'.join(('MUSE-{0} {1}'.format(id_, mult)).split()[:2])
    for id_, mult in zip(muse['orig_id'], muse['mult id'].filled(''))
]

muse.rename_column('z', 'zspec')

muse['ra'].format = '.6f'
muse['dec'].format = '.6f'

muse['id','ra','dec','zspec','zconf'].write(
    "2303.09568-lagattuta.csv",
    overwrite=True
)