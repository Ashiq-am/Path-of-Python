# import Pygal module
import pygal

# Creating an instance of Bar Plot
Bar_plot = pygal.Bar()

# Creating a bar Plot using random data
Bar_plot(1, 3, 3, 7)(1, 6, 6, 4).render_to_file('BarPlot.svg')
