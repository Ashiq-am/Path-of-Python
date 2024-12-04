import xlrd

# Open workbook
wb = xlrd.open_workbook('data.xls')

# Select a sheet
sheet = wb.sheet_by_name('Sheet1')

# Read data
li = []
for idx in range(sheet.nrows):
    row = sheet.row(idx)
    li.append([cell.value for cell in row])

print(li[:5])