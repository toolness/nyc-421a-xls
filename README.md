This is a set of simple scripts that help convert NYC's 
open data on [Properties With a 421a Exemption][421a], which is
in several separate Excel workbooks, into a single CSV file.

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

Tests can be run via `pytest`.

[421a]: https://www1.nyc.gov/site/finance/benefits/benefits-421a.page
[pipenv]: https://docs.pipenv.org/
