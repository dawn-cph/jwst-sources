# jwst-sources
Repository to keep track of individually published JWST sources, high-z or otherwise

# Notes

- Add a new reference with a `csv` and `meta` file in the `./tables` directory.
- see `tables/template.meta` for an example metadata file
  - `meta` files should have at a minimum, `arxiv` and `author` keys
  - `meta` files are read as YAML
  - ':' characters are special to YAML and not allowed in the parameter value strings
- `csv` files should have at a minimum, `id`, `ra`, `dec` columns, and ideally also `zphot` and/or `zspec`.  
  - `ra`, `dec` are intepreted as decimal degrees and should have a minimum of 6 and 5 decimal places, respectively
  - Alternatively, `rah` and `decd` columns can be provided with coordinates in sexagesimal format (HH:MM:SS.SS, DD:MM:SS.SS)
- `grizli` is a requirement, but the basic installation with `pip install grizli` should be enough without all of its dependencies

Test generating the master table with 

```bash 
$ python build.py
```

# App interface

The table is rendered in at https://jwst-sources.herokuapp.com/, with some tools for guerying and generating the unique source identifiers. 
 See https://jwst-sources.herokuapp.com/help.

# To Do

- Add function to query for matches in a local test table
- add `keywords` to meta, like `keywords: highz, quiescent`
- Build heroku app
  - Query for existing sources around a test position
  - Build a `jname` for a given RA/Dec
  - Display the table itself
