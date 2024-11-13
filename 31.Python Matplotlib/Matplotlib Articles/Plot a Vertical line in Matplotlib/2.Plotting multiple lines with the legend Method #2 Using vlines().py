# importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# defining an array
xs = [1, 100]

# defining plot size
plt.figure(figsize = (10, 7))

# multiple lines all full height
plt.vlines(x = [37, 37.25, 37.5], ymin = 0, ymax = max(xs),
		colors = 'purple',
		label = 'vline_multiple - full height')

# multiple lines with varying ymin and ymax
plt.vlines(x = [38, 38.25, 38.5], ymin = [0, 25, 75], ymax = max(xs),
		colors = 'teal',
		label = 'vline_multiple - partial height')

# single vline with full ymin and ymax
plt.vlines(x = 39, ymin = 0, ymax = max(xs), colors = 'green',
		label = 'vline_single - full height')

# single vline with specific ymin and ymax
plt.vlines(x = 39.25, ymin = 25, ymax = max(xs), colors = 'green',
		label = 'vline_single - partial height')

# place legend outside
plt.legend(bbox_to_anchor = (1.0, 1), loc = 'up')
plt.show()
