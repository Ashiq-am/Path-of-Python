# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# make an agg figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3])

plt.delaxes()

plt.suptitle('matplotlib.pyplot.delaxes() function Example',
             fontweight="bold")

plt.show()
