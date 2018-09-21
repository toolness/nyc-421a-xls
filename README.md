This is a set of simple scripts that help convert NYC's 
open data on [Properties With a 421a Exemption][421a], which is
in several separate Excel workbooks, into a single CSV file.

## CSV format

Here's some sample data from the big CSV file this generates:

| YEARS | BOROUGH NAME | BOROUGH | NEIGHBORHOOD | BUILDING CLASS CATEGORY | TAX CLASS AT PRESENT | BLOCK  | LOT   | BUILDING CLASS AT PRESENT | ADDRESS             | ZIP CODE | RESIDENTIAL UNITS | COMMERCIAL UNITS | TOTAL UNITS | LAND SQUARE FEET | GROSS SQUARE FEET | YEAR BUILT |
| ----- | ------------ | ------- | ------------ | ----------------------- | -------------------- | ------ | ----- | ------------------------- | ------------------- | -------- | ----------------- | ---------------- | ----------- | ---------------- | ----------------- | ---------- |
| 1415  | bronx        | 2.0     | BATHGATE     | 03  3-FAMILY            | 1.0                  | 3030.0 | 157.0 | C0                        | 410 EAST 183 STREET | 10458.0  | 3.0               | 0.0              | 3.0         | 2000.0           | 4872.0            | 2005.0     |

For more details on the format of the CSV file, see the
documentation in [`convert_to_csv.py`](convert_to_csv.py).

## Quick start

You will need Python 3.7 and [pipenv][].

Run:

```
pipenv install --python 3.7
pipenv shell
```

(Note that if you're on Windows and have `bash`, you
might want to run `pipenv run bash` instead of
`pipenv shell`, to avoid a bug whereby command-line
history doesn't work with `cmd.exe`.)

Then download all the Excel workbooks:

```
python download.py
```

This will download everything into the `data` directory.

Then, to create the big CSV file, run:

```
python convert_to_csv.py
```

The CSV will be placed in `data/421a.csv`.

## Tests

Tests can be run via `pytest`. Make sure you've run `download.py` before
running them, as they make use of the downloaded data.

[421a]: https://www1.nyc.gov/site/finance/benefits/benefits-421a.page
[pipenv]: https://docs.pipenv.org/
