# importing pygal
import pygal
from pygal.style import BlueStyle

# creating the chart object
bar = pygal.Bar(fill = True, style = BlueStyle)

# naming the title
bar.title = 'Bar Chart'

# Random data
bar.add('A', [26, 22, 39, 39, 32, 30, 33, 24, 24, 30])
bar.add('B', [31, 40, None, None, None, None, 40, 32, 25, 31])
bar.add('C', [37, 27, 31, 20, None, 32, 24, 39, 29, 22])
bar.add('D', [38, None, 20, 29, 33, 23, 32, 33, 32, 23])

bar
