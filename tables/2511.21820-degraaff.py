import astropy.table
tab = astropy.table.Table.read(
    "https://zenodo.org/records/17665942/files/deGraaff2025_lrds_withdups_blackbody_eline_fits.fits?download=1",
    format="fits"
)

tab["id"] = ["{pid}_{srcid}".format(**row) for row in tab]

tab["id","file","root","ra","dec","zspec"].write(
    "2511.21820-degraaff.csv",
    format="ascii.csv",
    overwrite=True,
)