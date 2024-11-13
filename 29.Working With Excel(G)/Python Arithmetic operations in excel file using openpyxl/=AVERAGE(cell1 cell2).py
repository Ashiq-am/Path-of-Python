import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 400
sheet['A4'] = 500
sheet['A5'] = 600

# The value in cell A7 is set to a formula
# that return average of the values in A1, A2, A3, A4, A5 .
sheet['A7'] = '= AVERAGE(A1:A5)'

wb.save("average.xlsx")
