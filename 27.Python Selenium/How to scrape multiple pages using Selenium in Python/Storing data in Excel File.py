with xlsxwriter.Workbook('result.xlsx') as workbook:
	worksheet = workbook.add_worksheet()

	for row_num, data in enumerate(element_list):
		worksheet.write_row(row_num, 0, data)
