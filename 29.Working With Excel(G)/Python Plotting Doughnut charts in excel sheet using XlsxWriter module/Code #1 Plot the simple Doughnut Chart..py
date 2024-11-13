''''''


'''For plotting the simple Pie chart on an excel sheet, use add_chart() method with type 
‘doughnut’ keyword argument of a workbook object.'''

# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('chart_doughnut1.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Create a new Format object to formats cells
# in worksheets using add_format() method .

# here we create bold format object .
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Category', 'Values']
data = [
    ['Glazed', 'Chocolate', 'Cream'],
    [50, 35, 15],
]

# Write a row of data starting from 'A1'
# with bold format .
worksheet.write_row('A1', headings, bold)

# Write a column of data starting from
# 'A2', 'B2' respectively .
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

# Create a chart object that can be added
# to a worksheet using add_chart() method.

# here we create a doughnut chart object .
chart1 = workbook.add_chart({'type': 'doughnut'})

# Add a data series to a chart
# using add_series method.

# Configure the first series.
# syntax to define ranges
# [sheetname, first_row, first_col, last_row, last_col].
chart1.add_series({
    'name': 'Doughnut sales data',
    'categories': ['Sheet1', 1, 0, 3, 0],
    'values': ['Sheet1', 1, 1, 3, 1],
})

# Add a chart title
chart1.set_title({'name': 'Popular Doughnut Types'})

# Set an Excel chart style. Colors
# with white outline and shadow.
chart1.set_style(10)

# add chart to the worksheet with an offset,
# at the top-left corner of a chart
# is anchored to cell C2 .
worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})

# Finally, close the Excel file
# via the close() method.
workbook.close()
