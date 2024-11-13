# Python3 code to write
# data to Excel
import xlwings as xw

# Selecting a sheet in Excel
ws = xw.Book('data.xlsx').sheets("Sheet2")

# Writing one value to
# one cell
ws.range("A1").value = "geeks"

# Writing multiple values
# to a cell for automatic
# data placement
ws.range("B1").value = ["for", "geeks"]

# Writing 2D data to a cell
# to automatically put data
# into correct cells
ws.range("A2").value = [[1, 2, 3], ['a', 'b', 'c']]

# Writing multiple data to
# multiple cells
ws.range("A4:C4").value = ["This", "is", "awesome"]

# Outputting entire table
print("Table :\n", ws.range("A1").expand().value)
