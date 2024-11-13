# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

# Data for the table
data = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[10, 11, 12],

]

# Creating the Table
worksheet.add_table('B2:D5', {'data': data})

workbook.close()
