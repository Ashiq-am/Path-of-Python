# ...

writer = pd.ExcelWriter("urls.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1", index=False)

workbook = writer.book
worksheet = writer.sheets["Sheet1"]

url_format = workbook.add_format({"font_color": "blue", "underline": 1})

for row_num in range(1, len(df) + 1):
	worksheet.write_url(row_num, 1, df.at[row_num - 1, "URL"], url_format)

# Save the Excel file
writer.close()
