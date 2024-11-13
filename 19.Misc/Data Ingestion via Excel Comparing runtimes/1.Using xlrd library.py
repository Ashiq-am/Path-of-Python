import xlrd
import time

# Time variable for finding the
# difference
t1 = time.time()

# Open the workbook to read the
# excel file
workbook = xlrd.open_workbook('excel.xls')

# Get the first sheet in the workbook
sheet = workbook.sheet_by_index(0)

# Read row data line by line
for i in range(sheet.nrows):
    row = sheet.row_values(i)
    print(row)

t2 = time.time()
print("\nTime taken by xlrd:")
print(t2 - t1)
