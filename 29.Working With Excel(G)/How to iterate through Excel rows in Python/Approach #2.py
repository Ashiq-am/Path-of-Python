# import module
import openpyxl

# load excel with its path
wrkbk = openpyxl.load_workbook("Book1.xlsx")

sh = wrkbk.active

# iterate through excel and display data
for row in sh.iter_rows(min_row=1, min_col=1, max_row=12, max_col=3):
	for cell in row:
		print(cell.value, end=" ")
	print()
