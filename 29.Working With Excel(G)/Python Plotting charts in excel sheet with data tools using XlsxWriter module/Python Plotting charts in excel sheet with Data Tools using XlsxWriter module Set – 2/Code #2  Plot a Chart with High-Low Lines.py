# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('Example5_chart.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Create a new Format object to formats cells
# in worksheets using add_format() method .

# here we create italic format object
italic = workbook.add_format({'italic': 1})

# Add the worksheet data that the charts will refer to.
Data1 = ['Subject', 'Mid Exam Score', 'End Exam Score']
Data2 = [
    ["Math", "Physics", "Computer",
     "Hindi", "English", "chemistry"],
    [90, 78, 60, 80, 60, 90],
    [45, 39, 30, 40, 30, 60]]

# Write a row of data starting from 'A1'
# with bold format .
worksheet.write_row('A1', Data1, italic)

# Write a column of data starting from
# 'A2', 'B2', 'C2' respectively
worksheet.write_column('A2', Data2[0])
worksheet.write_column('B2', Data2[1])
worksheet.write_column('C2', Data2[2])

# set the wdith of B and C column
worksheet.set_column('B:C', 15)

# Create a chart object that can be added
# to a worksheet using add_chart() method.

# here we create a line chart object .
chart2 = workbook.add_chart({'type': 'line'})

# Adding the High-Low lines.
chart2.set_high_low_lines()

# Add a data series to a chart
# using add_series method.

# Configure the first series.
# = Sheet1 !$A$1 is equivalent to ['Sheet1', 0, 0].

# note : spaces is not inserted in b / w
# = and Sheet1, Sheet1 and !
# if space is inserted it throws warning.
chart2.add_series({
    'categories': '= Sheet1 !$A$2:$A$7',
    'values': '= Sheet1 !$B$2:$B$7',
})

# Configure the second series.
chart2.add_series({
    'categories': '= Sheet1 !$A$2:$A$7',
    'values': '= Sheet1 !$C$2:$C$7',
})

# Add a chart title.
chart2.set_title({'name': 'Exam Score Distribution'})

# Add x-axis label
chart2.set_x_axis({'name': 'Subjects'})

# Add y-axis label
chart2.set_y_axis({'name': 'Marks'})

# Set an Excel chart style.
chart2.set_style(11)

# add chart to the worksheet with given
# offset values at the top-left corner of
# a chart is anchored to cell D2
worksheet.insert_chart('D2', chart2,
                       {'x_offset': 20, 'y_offset': 5})

# Finally, close the Excel file
# via the close() method.
workbook.close()
