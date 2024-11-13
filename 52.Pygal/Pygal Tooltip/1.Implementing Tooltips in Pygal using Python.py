import pygal

line_chart = pygal.Line()
line_chart.title = 'Revenue Changes(in %)'
line_chart.x_labels = map(str, range(2002, 2023))
line_chart.add('GeeksforGeeks', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1, None])
line_chart.render_to_file('line_chart.svg')
