# importing the modules
import matplotlib.pyplot as plt
import numpy as np

# specfying the plot size
plt.figure(figsize = (10, 5))

# only one line may be specified; full height
plt.axvline(x = 7, color = 'b', label = 'axvline - full height')

# only one line may be specified; ymin & ymax spedified as
# a percentage of y-range
plt.axvline(x = 7.25, ymin = 0.1, ymax = 0.90, color = 'r',
			label = 'axvline - % of full height')

# place legend outside
plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper left')

# rendering plot
plt.show()
