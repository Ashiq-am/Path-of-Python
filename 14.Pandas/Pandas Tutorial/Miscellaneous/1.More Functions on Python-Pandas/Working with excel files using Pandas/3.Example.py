sheet1 = pds.read_excel(file,
						sheet_name = 0,
						index_col = 0)

sheet2 = pds.read_excel(file,
						sheet_name = 1,
						index_col = 0)

newData = pds.concat([sheet1, sheet2])
