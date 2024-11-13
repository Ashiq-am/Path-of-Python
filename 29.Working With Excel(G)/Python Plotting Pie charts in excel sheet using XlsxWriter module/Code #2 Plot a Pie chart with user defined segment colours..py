''''''




"""For plotting the pie chart with user defined segment colours on an excel sheet, use add_series() method with points 
keyword argument of a chart object."""

# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('chart_pie_colour.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Create a new Format object to formats cells
# in worksheets using add_format() method .

# here we create bold format object .
bold = workbook.add_format({'bold': 1})

# create a data list .
headings = ['Category', 'Values']

data = [
    ['Apple', 'Cherry', 'Pecan'],
    [60, 30, 10],
]

# Write a row of data starting from 'A1'
# with bold format .
worksheet.write_row('A1', headings, bold)

# Write a column of data starting from
# A2, B2, C2 respectively.
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

# Create a chart object that can be added
# to a worksheet using add_chart() method.

# here we create a pie chart object
chart2 = workbook.add_chart({'type': 'pie'})

# Add a data series to a chart
# using add_series method.

# Configure the first series.
# = Sheet1 !$A$1 is equivalent to ['Sheet1', 0, 0].
chart2.add_series({
    'name': 'Pie sales data',
    'categories': '= Sheet1 !$A$2:$A$4',
    'values': '= Sheet1 !$B$2:$B$4',
    'points': [
        {'fill': {'color': '# 5ABA10'}},
        {'fill': {'color': '# FE110E'}},
        {'fill': {'color': '# CA5C05'}},
    ],
})

# Add a chart title.
chart2.set_title({'name': 'Pie Chart with user defined colors'})

# Insert the chart into the worksheet (with an offset)
# the top-left corner of a chart is anchored to cell C2.
worksheet.insert_chart('C2', chart2, {'x_offset': 25, 'y_offset': 10})

# Finally, close the Excel file
# via the close() method.
workbook.close()
