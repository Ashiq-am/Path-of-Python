''''''



'''For plotting a pie chart with user defined hole size on an excel sheet, use set_hole_size() method 
with definite value(radius) argument of the chart object.'''



# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('chart_doughnut4.xlsx')

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
chart4 = workbook.add_chart({'type': 'doughnut'})

# Configure the series.
chart4.add_series({
    'name': 'Doughnut sales data',
    'categories': '= Sheet1 !$A$2:$A$4',
    'values': '= Sheet1 !$B$2:$B$4',
})

# Set a 3D style.
chart4.set_style(26)

# Add a title.
chart4.set_title({'name': 'Doughnut Chart with small hole size'})

# Change the hole size.
chart4.set_hole_size(33)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('C2', chart4, {'x_offset': 25, 'y_offset': 10})

# Finally, close the Excel file
# via the close() method.
workbook.close()
