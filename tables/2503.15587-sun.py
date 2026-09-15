from grizli import utils

tab = utils.read_catalog("https://www.dropbox.com/scl/fi/blymeoghmeeaplnzpb0qh/sapphires_edr_spec_cat.fits?rlkey=cslzf1ym33si94x71kg5ve1cl&st=p0m37jhr&e=1&dl=1", format="fits")

for c in list(tab.colnames):
    tab.rename_column(c, c.lower())

tab.write("2503.15587-sun.csv", overwrite=True)