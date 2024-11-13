import pygal
from pygal.style import Style

# change graph color
custom_style = Style(colors=('#E80080', '#404040', '#9BC850', '#ffeb44', '#ff00ff'))


# creating Pie chart object
pie_chart = pygal.Pie(inner_radius=1, style=custom_style)

pie_chart.title = 'Number of people using social media (in million)'
pie_chart.add('Signal', 14.36)
pie_chart.add('Instagram', 26.01)
pie_chart.add('Twitter', 8.8)
pie_chart.add('Facebook', 30.32)
pie_chart.add('Youtube', 20.3)

pie_chart.render_to_png('aa.png')
