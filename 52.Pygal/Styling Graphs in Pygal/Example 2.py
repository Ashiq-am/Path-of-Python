# importing pygal
import pygal
from pygal.style import LightSolarizedStyle

# creating the chart object
line = pygal.StackedLine(fill = True, style = LightSolarizedStyle)

# naming the title
line.title = 'Stacked Line'

# Random data
line.add('A', [26, 22, 39, 39, 32, 30, 33, 24, 24, 30])
line.add('B', [31, 40, None, None, None, None, 40, 32, 25, 31])
line.add('C', [37, 27, 31, 20, None, 32, 24, 39, 29, 22])
line.add('D', [38, None, 20, 29, 33, 23, 32, 33, 32, 23])

line
