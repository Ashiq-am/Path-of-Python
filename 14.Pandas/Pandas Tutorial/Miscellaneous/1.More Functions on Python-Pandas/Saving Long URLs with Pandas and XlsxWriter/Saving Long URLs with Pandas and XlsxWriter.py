import pandas as pd
data = {
    "Description": ["GeeksForGeeks", "Python Documentation", "Pandas Documentation"],
    "URL": [
        "https://www.geeksforgeeks.org/",
        "https://docs.python.org/3/",
        "https://pandas.pydata.org/docs/"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Specify the Excel writer and the engine
writer = pd.ExcelWriter("urls.xlsx", engine="xlsxwriter")

# Write the DataFrame to the Excel file
df.to_excel(writer, sheet_name="Sheet1", index=False)

# Access the XlsxWriter workbook and worksheet objects
workbook = writer.book
worksheet = writer.sheets["Sheet1"]

# Apply URL formatting to the URL column
url_format = workbook.add_format({"font_color": "blue", "underline": 1})

# Format the 'URL' column as clickable hyperlinks
for row_num in range(1, len(df) + 1):
    worksheet.write_url(row_num, 1, df.at[row_num - 1, "URL"], url_format)

# Adjust column widths
for column in df:
    column_length = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    worksheet.set_column(col_idx, col_idx, column_length + 2)

# Save the Excel file
writer.close()
