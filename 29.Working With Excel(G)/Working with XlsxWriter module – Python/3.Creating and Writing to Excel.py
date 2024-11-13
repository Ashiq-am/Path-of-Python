# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

content = ["Welcome", "to", "Geeks", "for", "Geeks"]

# Writing to row and column respectively
worksheet.write_row(0, 1, content)
worksheet.write_column(1, 0, content)

workbook.close()
