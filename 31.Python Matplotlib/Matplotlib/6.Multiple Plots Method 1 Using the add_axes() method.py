# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))

# Creating first axes for the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Creating second axes for the figure
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])

# Adding the data to be plotted
ax1.plot([5, 4, 3, 2, 1], [2, 3, 4, 5, 6])
ax2.plot([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])

plt.show()
