import ipywidgets as wdg

# Real time interactive squae calculation
wdg.interact(lambda x:x**2, x = wdg.IntSlider(min = 0, max = 10, value = 1))
