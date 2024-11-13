import ipywidgets as widgets
widgets.interact(lambda x:x, x = widgets.FloatLogSlider(description ="$e ^ x$", min = 0, step = 1, base = 5, max = 10, value = 1))
