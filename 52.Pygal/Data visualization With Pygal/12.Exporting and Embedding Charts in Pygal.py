import pygal

bar_chart = pygal.Bar()
bar_chart.add('Cats', [1, 2, 3])
svg_data = bar_chart.render()

with open('chart.html', 'w') as file:
    file.write(f'<html><body>{svg_data}</body></html>')
