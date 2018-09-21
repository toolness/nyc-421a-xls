import xlrd
import csv

from download import DATA_DIR

OUTFILE = DATA_DIR / "421a.csv"

BOROUGHS = [
    'manhattan',
    'queens',
    'statenisland',
    'brooklyn',
    'bronx'
]

COLUMNS = [
    "BOROUGH",
    "NEIGHBORHOOD",
    "BUILDING CLASS CATEGORY",
    "TAX CLASS AT PRESENT",
    "BLOCK",
    "LOT",
    "BUILDING CLASS AT PRESENT",
    "ADDRESS",
    "ZIP CODE",
    "RESIDENTIAL UNITS",
    "COMMERCIAL UNITS",
    "TOTAL UNITS",
    "LAND SQUARE FEET",
    "GROSS SQUARE FEET",
    "YEAR BUILT"
]

def itersheetrows():
    for f in DATA_DIR.glob('*.*'):
        if not (f.name.endswith('.xlsx') or f.name.endswith('.xls')):
            continue
        bmatches = [borough for borough in BOROUGHS if borough in f.name]
        if not bmatches:
            continue
        xlsfile = f
        book = xlrd.open_workbook(str(xlsfile))
        for sheet in book.sheets():
            found = False
            for i in range(sheet.nrows):
                row = sheet.row(i)
                rowvals = [cell.value for cell in row]
                if COLUMNS == rowvals:
                    print(f"In {xlsfile.name} sheet '{sheet.name}', found header row at row {i}.")
                    found = True
                elif found:
                    yield rowvals
            if not found:
                print(f"Alas, header row was not found in {xlsfile.name} sheet '{sheet.name}'.")


if __name__ == '__main__':
    with OUTFILE.open('w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rownum = 0
        for row in itersheetrows():
            print(f"Writing row {rownum}.")
            writer.writerow(row)
            rownum += 1
