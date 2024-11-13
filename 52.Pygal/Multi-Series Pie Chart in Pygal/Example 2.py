# importing pygal
import pygal


# creating pie_chart object
pie_chart = pygal.Pie()
pie_chart.title = 'Pie Chart'

# random data
pie_chart.add("A", [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
pie_chart.add("B", [0, 1, 1, 2, 3, 7, 5, 10, 20, 32, 35])
pie_chart.add("C", [0, 1, 1, 4, 5, 5.5, 7, 12, 26, 24, 45])

pie_chart
