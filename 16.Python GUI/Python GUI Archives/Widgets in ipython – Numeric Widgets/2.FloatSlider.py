import ipywidgets as widgets
widgets.interact(lambda x:x**2, x = widgets.FloatSlider(min = 0, step =.25, max = 10, value = 1))
