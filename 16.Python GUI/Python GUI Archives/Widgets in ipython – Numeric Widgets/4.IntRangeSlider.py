import ipywidgets as widgets
widgets.interact(lambda x :x, x = widgets.IntRangeSlider(min = 0, step = 1, max = 10, value =[1, 2]))
