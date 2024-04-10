from grizli import utils
import astropy.table

raw = utils.GTable.read('https://raw.githubusercontent.com/dalekocevski/Kocevski24/main/Kocevski24.Table3.dat', format='ascii', names=['field','xid', 'ra', 'dec', 'zbest', 'zflag', 'beta_UV', 'beta_UV_err', 'beta_opt', 'beta_opt_err', 'mag444', 'm_uv', 'M_UV'])

raw['id'] = ['{field}-{xid}'.format(**row) for row in raw]

zsp = raw['zflag'] == 1
raw['zphot'] = -1.
raw['zphot'][~zsp] = raw['zbest'][~zsp]
raw['zspec'] = -1.
raw['zspec'][zsp] = raw['zbest'][zsp]

raw.remove_columns(['field','xid','zbest','zflag'])

raw.write('2404.03576-kocevski.csv', overwrite=True)
