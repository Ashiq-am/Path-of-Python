# import module
import xlwt
from datetime import datetime

# assign attributes
style0 = xlwt.easyxf('font: name Verdana, color-index green, bold on',)
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
style2 = xlwt.easyxf(
	'font: name Times New Roman, color-index orange, bold on',)


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

# add data
ws.write(0, 0, 156, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1, style2)
ws.write(2, 1, 1, style2)
ws.write(2, 2, xlwt.Formula("A3+B3"))

# printing results
wb.save('example.xls')
