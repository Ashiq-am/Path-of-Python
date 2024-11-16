# import pandas lib as pd
import pandas as pd

# Create a Pandas dataframe from some data.
dataframe = pd.DataFrame(
	{'Marks (Out of 50)': [30, 40, 45, 15, 8, 5, 35],
	'Percentage': [.6, .8, .9, .3, .16, .1, .7 ], })

# Create a Pandas Excel writer
# object using XlsxWriter as the engine.
writer_object = pd.ExcelWriter("Example_column.xlsx",
								engine ='xlsxwriter')

# Write a dataframe to the worksheet.
dataframe.to_excel(writer_object, sheet_name ='Sheet1')

# Create xlsxwriter workbook object .
workbook_object = writer_object.book

# Create xlsxwriter worksheet object
worksheet_object = writer_object.sheets['Sheet1']

# Create a new Format object to formats cells
# in worksheets using add_format() method .

# number taken upto 2 decimal places
# format object is create.
format_object1 = workbook_object.add_format({'num_format': '# 0.00'})

# Integral percentage format object is create.
format_object2 = workbook_object.add_format({'num_format': '0 %'})

# Note: It isn't possible to format
# any cells that already have a format
# such as the index or headers or any
# cells that contain dates or datetimes.

# Set the column width and format.
worksheet_object.set_column('B:B', 20, format_object1)

# Set the column width and format.
worksheet_object.set_column('C:C', 15, format_object2)

# Close the Pandas Excel writer
# object and output the Excel file.
writer_object.save()
