# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


fig = plt.figure(figsize = (5, 4))

# Adding the axes to the figure
ax = fig.add_axes([1, 1, 1, 1])

# plotting 1st dataset to the figure
ax1 = ax.plot([1, 2, 3, 4], [1, 2, 3, 4])

# plotting 2nd dataset to the figure
ax2 = ax.plot([1, 2, 3, 4], [2, 3, 4, 5])

plt.show()
