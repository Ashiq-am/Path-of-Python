# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))

# Creating a new axes for the figure
ax = fig.add_axes([1, 1, 1, 1])

# Adding the data to be plotted
ax.plot([2, 3, 4, 5, 5, 6, 6], [5, 7, 1, 3, 4, 6 ,8])
plt.show()
