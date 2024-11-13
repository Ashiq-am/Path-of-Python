import pygal

bar_chart = pygal.Bar()
bar_chart.add('Series 1', [1, 2, 3])
bar_chart.add('Series 2', [3, 2, 1])
bar_chart.render_to_file('bar_chart.svg')
