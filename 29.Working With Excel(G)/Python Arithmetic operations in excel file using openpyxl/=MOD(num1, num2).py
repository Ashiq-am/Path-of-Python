import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

# The value in cell is set to a formula
# that gives remainder or modulus value.
sheet['A1'] = '= MOD(64, 8)'
sheet['A2'] = '= MOD(25, 4)'

wb.save("modulus.xlsx")
