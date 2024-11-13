# Python program to
# access Excel files

# Import required library
import xlwings as xw

# Opening an excel file
wb = xw.Book('data.xlsx')

# Viewing available
# sheets in it
wks = xw.sheets
print("Available sheets :\n", wks)

# Selecting a sheet
ws = wks[0]

# Selecting a value
# from the selected sheet
val = ws.range("A1").value
print("A value in sheet1 :", val)
