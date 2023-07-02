"""
Reformat Hainline et al. catalog
"""
from grizli import utils
import astropy.io.fits as pyfits
url = 'https://zenodo.org/record/8092529/files/JADES_DEEP_z_gt_8_Candidates_Hainline_et_al.fits?download=1'
tab = utils.read_catalog(url, format='fits')

tab['ra'] = tab['RA']
tab['dec'] = tab['DEC']
tab['zphot'] = tab['EAZY_z_a']
tab['zspec'] = tab['z_spec']
tab['id'] = tab['JADES_ID']
tab['Muv'] = tab['MUV']
tab['mag'] = 31.4 - 2.5*np.log10(tab['NRC_F444W_flux'])

tab['Muv'].format = '.2f'

tab['id','ra','dec','zphot','zspec','z_spec_source','Muv','mag'].write('2306.02468-hainline.csv', overwrite=True)