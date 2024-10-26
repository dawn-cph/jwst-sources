from astroquery.mast import Observations
from grizli import utils

all_obs = Observations.query_criteria(provenance_name="wide")
# data_products = Observations.get_product_list(all_obs)

all_obs['id'] = all_obs['target_name']
all_obs['ra'] = all_obs['s_ra']
all_obs['dec'] = all_obs['s_dec']

un = utils.Unique(all_obs['id'], verbose=False)

gratings = []
for i, v in enumerate(un.values):
    gi = [f.split('_')[-3] for f in all_obs[un[v]]['dataURL']]
    gratings.append(' '.join(gi))

print(f'maseda wide: {len(all_obs)} rows, {un.N} unique objects')

all_obs = all_obs[un.unique_index()]

all_obs['gratings'] = gratings
all_obs['id','ra','dec','gratings'].write('2403.05506-maseda.csv', overwrite=True)

# https://mast.stsci.edu/portal/Download/file/ 
# HLSP/wide/images/hlsp_wide_jwst_nirspec_{id}_clear-prism_v1.0_2nod.png