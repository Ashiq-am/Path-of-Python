import pygal

bar_chart = pygal.Bar()
bar_chart.add('Category A', [1, 3, 5, 7])
bar_chart.add('Category B', [2, 4, 6, 8])
bar_chart.render_to_file('bar_chart.svg')
