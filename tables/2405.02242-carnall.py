from grizli import utils

# https://academic.oup.com/mnras/article/534/1/325/7756422#supplementary-data
tab = utils.read_catalog("https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mnras/534/1/10.1093_mnras_stae2092/1/stae2092_supplemental_file.txt?Expires=1739386241&Signature=SDM5katQvIX-j-CmJQLG85ZelaHFBG3HsmNvNpdWsCUf5Y8RatenDGSZullzJuB0GytkIsT6GsUSHeMczUuT2CD-OpC-f9ssTA~Iv9kAYCxRFis4UnKVTOMLQyzim4mj-VE4EiHHl~3xxfHWpBdeuZfTuCh2CQv6jFBC0zQPlkVj-DClpvAK7cTeJoBQx482RnOHPKfc-~FnH9bDJdKeHbZgAImKZKEjgLmZYv5maiXtymD31vZZLtmR9EmQ5IldM40XBm0Hebqq9uVwnetDbuPdJwoI4I9sIsYqgYMyZM4b5sBOS99j8TSB1ny3xapbqZKk-ATRxw8fY4yjAI279A__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA", format="ascii.commented_header")

tab['zspec'] = tab["z_excels_v1"]
tab.write("2405.02242-carnall.csv", format="csv")