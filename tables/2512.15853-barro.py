import astropy.table
tab = astropy.table.Table.read(
    "https://github.com/guillermobc/Barro25/raw/refs/heads/main/Barro25_LRD_NIRSpec_bestfit_properties.fits",
    format="fits"
)

tab["id"] = tab['DJA_ID']

tab["id","ra","dec","zspec"].write(
    "2512.15853-barro.csv",
    format="ascii.csv",
    overwrite=True,
)