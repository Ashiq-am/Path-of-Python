# importing pygal
import pygal
import numpy


# creating the chart object
funnel = pygal.Funnel(legend_at_bottom=True, legend_at_bottom_columns=4)

# Random data
funnel.add('Red', numpy.random.rand(5))
funnel.add('Blue', numpy.random.rand(5))
funnel.add('Green', numpy.random.rand(5))
funnel.add('Yellow', numpy.random.rand(5))


# naming the title
funnel.title = 'Funnel Chart'

funnel.render_to_png('aa.png')
