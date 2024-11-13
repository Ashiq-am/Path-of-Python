# importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# defining an array
xs = [1, 100]

# defining plot size
plt.figure(figsize = (10, 7))

# single line
plt.vlines(x = 37, ymin = 0, ymax = max(xs),
		colors = 'purple',
		label = 'vline_multiple - full height')

plt.show()
