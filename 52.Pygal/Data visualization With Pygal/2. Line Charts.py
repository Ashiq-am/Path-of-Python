import pygal

line_chart = pygal.Line()
line_chart.add('Series 1', [1, 3, 5, 7])
line_chart.add('Series 2', [2, 4, 6, 8])
line_chart.render_to_file('line_chart.svg')
