import pygal

box_plot = pygal.Box()
box_plot.add('Data', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
box_plot.render_to_file('box_plot.svg')
