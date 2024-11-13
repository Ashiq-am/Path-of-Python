import ipywidgets as widgets
widgets.interact(lambda x :x, x = widgets.FloatRangeSlider(min = 0, step =.25, max = 10, value =[1, 2]))
