"""
Send to DJA database
"""

import numpy as np
from grizli import utils
from grizli.aws import db

def update_db_table():
    """
    """
    src = utils.read_catalog("jwst-sources.csv")

    osrc = db.SQL("select * from jwst_sources")
    okey = ["{arxiv} {jname}".format(**row) for row in osrc["arxiv", "jname"]]

    print(f"{len(osrc)} existing rows in db.jwst_sources")

    key = ["{arxiv} {jname}".format(**row) for row in src["arxiv", "jname"]]

    is_new = ~np.isin(key, okey)

    print(f"ntot={len(src)} in jwst-sources.csv, send {is_new.sum()} new rows")

    db.send_to_database(
        "jwst_sources",
        src["arxiv", "author", "ra", "dec", "jname", "zspec", "id"][is_new],
        if_exists="append",
    )

    return src, is_new

if __name__ == "__main__":
    update_db_table()

