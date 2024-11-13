# importing pygal
import pygal


# creating line chart object
pie_chart = pygal.Pie(inner_radius = .4)

# naming the title
pie_chart.title = 'Donut chart'

# random data
pie_chart.add('A', 10)
pie_chart.add('B', 20)
pie_chart.add('C', 30)
pie_chart.add('D', 40)

pie_chart
