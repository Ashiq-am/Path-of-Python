import pygal

pie_chart = pygal.Pie(tooltip_border_radius=10)
pie_chart.add('Part A', 10)
pie_chart.add('Part B', 20)
pie_chart.add('Part C', 30)
pie_chart.render_to_file('pie_chart.svg')
