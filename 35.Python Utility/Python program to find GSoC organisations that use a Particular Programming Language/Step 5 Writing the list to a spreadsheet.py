wb = openpyxl.Workbook()
sheet = wb['Sheet']

for i in range(0, len(orgElem)):
	sheet.cell(row = i + 1, column = 1).value = orgElem[i].getText()
	sheet.cell(row = i + 1, column = 2).value = languageCheck[i]
	sheet.cell(row = i + 1, column = 3).value = orgURL[i]

wb.save('gsocOrgsList.xlsx')
