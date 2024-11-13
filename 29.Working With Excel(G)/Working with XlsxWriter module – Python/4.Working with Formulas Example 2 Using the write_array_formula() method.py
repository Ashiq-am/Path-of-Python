# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

content = [1, 2, 3, 4, 5]

# Writing to row and column respectively
worksheet.write_row(0, 1, content)
worksheet.write_column(1, 0, content)

# Using the array formula to find the
# sum and the product of the given cells
worksheet.write_array_formula('A7', '{=SUM(A1:A6)}')
worksheet.write_array_formula('G1', '{=PRODUCT(B1:F1)}')

workbook.close()
