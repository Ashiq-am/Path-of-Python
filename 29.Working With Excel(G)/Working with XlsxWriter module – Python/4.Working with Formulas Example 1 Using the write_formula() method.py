# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

content = [1, 2]

# Writing to row and column respectively
worksheet.write_row(0, 1, content)
worksheet.write_column(1, 0, content)

# Using the array formula to find the
# sum and the product of the given cells
worksheet.write_formula('A4', '{=SUM(A2, A3)}')
worksheet.write_formula('D1', '{=PRODUCT(B1, C1)}')

workbook.close()
