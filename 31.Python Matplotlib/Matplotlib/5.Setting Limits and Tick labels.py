# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


x = [3, 1, 3]
y = [3, 2, 1]

# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))

# Creating first axes for the figure
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Adding the data to be plotted
ax.plot(x, y)

ax.set_xlim(1, 2)

ax.set_xticklabels((
	"one", "two", "three", "four", "five", "six"))

plt.show()
