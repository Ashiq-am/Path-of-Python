import pygal

data = {'Cats': [1, 2, 3], 'Dogs': [4, 5, 6]}
bar_chart = pygal.Bar()
for key, values in data.items():
    bar_chart.add(key, values)
bar_chart.render_to_file('bar_chart.svg')
