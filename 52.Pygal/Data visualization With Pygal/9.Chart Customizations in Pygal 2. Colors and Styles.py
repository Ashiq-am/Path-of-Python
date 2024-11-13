import pygal
from pygal.style import Style

custom_style = Style(
    colors=['#E80080', '#404040'],
    background='#FFFFFF',
    plot_background='#EFEFEF',
    opacity='.6',
    label_font_size=14,
)

bar_chart = pygal.Bar(style=custom_style)
bar_chart.add('Category A', [1, 3, 5, 7])
bar_chart.add('Category B', [2, 4, 6, 8])
bar_chart.render_to_file('bar_chart.svg')
