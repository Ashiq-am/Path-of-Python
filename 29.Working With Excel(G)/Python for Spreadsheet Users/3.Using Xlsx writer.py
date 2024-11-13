# import module
import xlsxwriter

# Create an new Excel file and add a
# worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
ws = workbook.add_worksheet()

# Widen the first column to make the
# text clearer.
ws.set_column('A:A', 20)

# Adding a bold format to use to highlight
# cells.
style = workbook.add_format({'bold': True})

# add data
ws.write('A1', 'Geeks')
ws.write('A2', 'for Geeks', style)
ws.insert_image('B5', 'logo.png')

workbook.close()
