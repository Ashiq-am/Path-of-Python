# importing pygal
import pygal


# creating line chart object
pie_chart = pygal.Pie(half_pie = True)

# naming the title
pie_chart.title = 'Half Pie chart'


# random data
pie_chart.add('A', 115)
pie_chart.add('B', 322)
pie_chart.add('C', 834)
pie_chart.add('D', 21)

pie_chart
