# importing pygal
import pygal
import pandas


# creating the chart object
bar_chart = pygal.StackedBar()

# naming the title
bar_chart.title = 'Stacked Bar chart'

df = pandas.read_csv('Iris.csv')

bar_chart.add("SepalLengthCm", df['SepalLengthCm'])
bar_chart.add("PetalLengthCm", df['PetalLengthCm'])
bar_chart
