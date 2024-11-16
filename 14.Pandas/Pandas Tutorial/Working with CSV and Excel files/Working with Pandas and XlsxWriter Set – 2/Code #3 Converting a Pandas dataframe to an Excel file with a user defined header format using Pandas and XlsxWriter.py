# import pandas lib as pd
import pandas as pd


data1 = ["Math", "Physics", "Computer",
		"Hindi", "English", "chemistry"]
data2 = [95, 78, 80, 80, 60, 95]
data3 = [90, 67, 78, 70, 63, 90]

# Create a Pandas dataframe from some data.
dataframe = pd.DataFrame(
	{'Subject': data1,
	'Mid Term Exam Scores Out of 100' : data2,
	'End Term Exam Scores Out of 100' : data3})

# Create a Pandas Excel writer
# object using XlsxWriter as the engine.
writer_object = pd.ExcelWriter("Example_header.xlsx",
								engine ='xlsxwriter')

# Write a dataframe to the worksheet.
# we turn off the default header
# and skip one row because we want
# to insert a user defined header there.
dataframe.to_excel(writer_object, sheet_name ='Sheet1',
						startrow = 1, header = False)

# Create xlsxwriter workbook object .
workbook_object = writer_object.book

# Create xlsxwriter worksheet object
worksheet_object = writer_object.sheets['Sheet1']

# Create a new Format object to formats cells
# in worksheets using add_format() method .

# here we create a format object for header.
header_format_object = workbook_object.add_format({
								'bold': True,
								'italic' : True,
								'text_wrap': True,
								'valign': 'top',
								'font_color': 'red',
								'border': 2})

# Write the column headers with the defined format.
for col_number, value in enumerate(dataframe.columns.values):
	worksheet_object.write(0, col_number + 1, value,
							header_format_object)

# Close the Pandas Excel writer
# object and output the Excel file.
writer_object.save()
