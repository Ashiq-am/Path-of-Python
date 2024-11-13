# importing pygal
import pygal
import pandas


# creating the chart object
radar_chart = pygal.Radar()

# naming the title
radar_chart.title = 'Radar chart'

df = pandas.read_csv('Iris.csv')

radar_chart.add("SepalLengthCm", df['SepalLengthCm'])
radar_chart.add("PetalLengthCm", df['PetalLengthCm'])
radar_chart
