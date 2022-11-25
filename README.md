# messy-excel
Pandas Wrapper for splitting read_excel resulting DataFrame by Extra Spaces

## Purpose
We noticed that especially in Japan, the format of Excel files are very messy.
Multiple tables are displayed in one sheet and thus makes it hard for pandas read_excel function to detect the multiple tables.
The read_html function does this perfectly well, as the `<table>` tags can tell us from and to where the data exists in one table.
This wrapper library is an attempt to make the post-load process easier by splitting the dataframes into multiple by detecting extra spaces.

## Disclaimer
This library is currently made in very simple logic. It is not meant to be used in production level. An extra row or columns that consists of no data, will be detected as an extra space/splitter and will create new dataframes based on it.

Any contributions to this project is welcome!

## Get Started
```python
from messy_excel import MessyExcel

# load data
me = MessyExcel('test_file.xlsx')
# datalist property will contains list of DataFrames
print(me.datalist[0])
```