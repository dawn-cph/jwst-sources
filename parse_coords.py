def parse_coords(coo):
    """
    Parse `?coords={ra},{dec}` input
    """
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    
    cc = coo.strip()
    if ',' in cc:
        cc = cc.split(',')
    else:
        cc = cc.split(' ')
    
    if ':' in cc[0]:
        crd = SkyCoord(' '.join(cc), unit=('hour','deg'))
        ra, dec = crd.ra.degree, crd.dec.degree
    else:
        ra, dec = float(cc[0]), float(cc[1])
    
    return ra, dec
