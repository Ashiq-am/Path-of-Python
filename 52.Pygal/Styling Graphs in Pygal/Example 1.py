# importing pygal
import pygal
from pygal.style import NeonStyle

# creating the chart object
funnel = pygal.Funnel(style = NeonStyle)

# naming the title
funnel.title = 'Funnel'

# Random data
funnel.add('A', [26, 22, 39, 39, 32, 30, 33, 24, 24, 30])
funnel.add('B', [31, 40, None, None, None, None, 40, 32, 25, 31])
funnel.add('C', [37, 27, 31, 20, None, 32, 24, 39, 29, 22])
funnel.add('D', [38, None, 20, 29, 33, 23, 32, 33, 32, 23])

funnel
