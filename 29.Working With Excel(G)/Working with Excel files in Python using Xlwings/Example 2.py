# Python3 code to select
# data from excel
import xlwings as xw

# Specifying a sheet
ws = xw.Book("data.xlsx").sheets['Sheet1']

# Selecting data from
# a single cell
v1 = ws.range("A2").value
v2 = ws.range("A3").value
print("Result :", v1, v2)

# Selecting entire
# rows and columns
r = ws.range("4:4").value
print("Row :", r)

c = ws.range("C:C").value
print("Column :", c)

# Selecting a 2D
# range of data
table = ws.range("A1:C4").value
print("Table :", table)

# Automatic table
# detection from
# a cell
automatic = ws.range("A1").expand().value
print("Automatic Table :", automatic)
