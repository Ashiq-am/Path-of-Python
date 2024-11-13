import xlwt
import xlrd
from xlutils.copy import copy

# load the excel file
rb = xlrd.open_workbook('UserBook.xls')

# copy the contents of excel file
wb = copy(rb)

# open the first sheet
w_sheet = wb.get_sheet(0)

# row number = 0 , coloumn number = 1
w_sheet.write(0,1,'Modified !')

# save the file
wb.save('UserBook.xls')
