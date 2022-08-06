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

Test the build with 

```bash 
$ python build.py
```
