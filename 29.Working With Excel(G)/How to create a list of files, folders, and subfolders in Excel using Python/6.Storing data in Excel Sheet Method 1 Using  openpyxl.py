# Function will create an excel file and
# write the file/ folder names and their
# path using openpyxl
def create_excel_using_openpyxl(name_list, path_list,
								path):

	# Creates a workbook object and gets an
	# active sheet
	work_book = Workbook()
	work_sheet = work_book.active

	# Writing the data in excel sheet
	row, col1_width, col2_width = 0, 0, 0
	while row <= len(name_list):
		name = work_sheet.cell(row=row+1, column=1)
		path = work_sheet.cell(row=row+1, column=2)

		# Writing the Heading i.e Name and Path
		if row == 0:
			name.value = "Name"
			path.value = "Path"
			row += 1
			continue

		# Writing the data from specified lists to colums
		name.value = name_list[row-1]
		path.value = path_list[row-1]

		# Adjusting width of Column in excel sheet
		col1_width = max(col1_width, len(name_list[row-1]))
		col2_width = max(col2_width, len(path_list[row-1]))
		work_sheet.column_dimensions["A"].width = col1_width
		work_sheet.column_dimensions["B"].width = col2_width
		row += 1

	# Saving the workbook
	work_book.save(filename="Final.xlsx")

create_excel_using_openpyxl(name_list, path_list, path)
