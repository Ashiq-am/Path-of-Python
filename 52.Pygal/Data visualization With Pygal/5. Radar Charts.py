import pygal

radar_chart = pygal.Radar()
radar_chart.add('Series 1', [1, 2, 3, 4])
radar_chart.add('Series 2', [4, 3, 2, 1])
radar_chart.render_to_file('radar_chart.svg')
