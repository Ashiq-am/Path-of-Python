import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 400
sheet['A4'] = 500
sheet['A5'] = 600

# The value in cell A7 is set to a formula
# that gives counting of number present in the cells.
sheet['A7'] = '= COUNT(A1:A6)'

wb.save("count.xlsx")
