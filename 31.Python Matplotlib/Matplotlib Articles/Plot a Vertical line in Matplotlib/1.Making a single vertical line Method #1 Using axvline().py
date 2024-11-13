# importing the modules
import matplotlib.pyplot as plt
import numpy as np

# specfying the plot size
plt.figure(figsize = (10, 5))

# only one line may be specified; full height
plt.axvline(x = 7, color = 'b', label = 'axvline - full height')

# rendering plot
plt.show()
