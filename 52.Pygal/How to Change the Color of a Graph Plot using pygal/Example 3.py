# importing pygal
import pygal
from pygal.style import Style

# change graph color
custom_style = Style(colors=('#ffebcd', '#daa520', '#9BC850', '#ffeb44', '#ff00ff'))

# creating Dot chart object
pie_chart = pygal.Dot(style=custom_style)

# chart data
pie_chart.add('Hindu', 13.36)
pie_chart.add('Muslim', 21.01)
pie_chart.add('Buddhist', 5.8)
pie_chart.add('Christian', 33.32)
pie_chart.add('Others', 26.3)

# naming the title
pie_chart.title = 'World religion population in 2007 (in %)'

pie_chart.render_to_png('aa.png')
