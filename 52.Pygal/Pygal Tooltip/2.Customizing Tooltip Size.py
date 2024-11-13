import pygal
from pygal.style import Style

# Define your own style
custom_style = Style(tooltip_font_size = 16,)

# Use this style
chart = pygal.Bar(style=custom_style)
chart.add('GeeksforGeeks Results', [1, 3, 3, 7])
chart.render_to_file('bar_chart.svg')
