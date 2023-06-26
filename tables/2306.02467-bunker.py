"""
Parse table from 2207.12446, Bunker et al. (2023)

https://archive.stsci.edu/hlsp/jades

"""
from grizli import utils

tab = utils.read_catalog('https://archive.stsci.edu/hlsps/jades/catalogs/hlsp_jades_jwst_nirspec_goods-s-deephst_clear-prism_line-fluxes_v1.0_catalog.fits')

tab['id'] = tab['NIRSpec_ID']
tab['zspec'] = tab['z_Spec'].filled(-1)
tab['ra'] = tab['RA_NIRCam']
tab['dec'] = tab['Dec_NIRCam']

fill = tab['ra'].mask & True
tab['ra'][fill] = tab['RA_TARG'][fill]
tab['dec'][fill] = tab['Dec_TARG'][fill]

tab['NIRCam_ID'].fill_value = -1
tab['z_Spec_flag'].fill_value = 'NA'
tab['z_PRISM'].fill_value = -1

tab['id','NIRCam_ID','ra','dec','zspec','z_Spec_flag','z_PRISM'].filled().write('2306.02467-bunker.csv', overwrite=True)