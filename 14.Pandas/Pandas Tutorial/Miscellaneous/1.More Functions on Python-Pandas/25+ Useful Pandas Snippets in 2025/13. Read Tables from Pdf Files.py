import camelot
tables = camelot.read_pdf('file.pdf')
df = tables[0].df       # Get the first table as a DataFrame
