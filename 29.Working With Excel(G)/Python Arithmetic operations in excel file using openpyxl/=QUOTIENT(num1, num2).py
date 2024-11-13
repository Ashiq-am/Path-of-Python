import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

# The value in cell is set to a formula
# that gives quotient value .
sheet['A1'] = '= QUOTIENT(64, 8)'
sheet['A2'] = '= QUOTIENT(25, 4)'

wb.save("quotient.xlsx")
