# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

content = [1, 2, 3, 5, 3, 2, 2]

# Writing to row and column respectively
worksheet.write_column(0, 0, content)

# Creating the chart object of type bar
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart
chart.add_series({'values': '=Sheet1!$A$1:$A$7',
				'marker': {'type': 'diamond'},})

# Insert the chart into the worksheet
worksheet.insert_chart('C1', chart)

workbook.close()
