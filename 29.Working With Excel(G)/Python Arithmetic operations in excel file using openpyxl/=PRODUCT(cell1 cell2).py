import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 2
sheet['A2'] = 3
sheet['A3'] = 4
sheet['A4'] = 5
sheet['A5'] = 6

# The value in cell A7 is set to a formula
# that multiplies the values in A1, A2, A3, A4, A5 .
sheet['A7'] = '= PRODUCT(A1:A5)'

wb.save("product.xlsx")
