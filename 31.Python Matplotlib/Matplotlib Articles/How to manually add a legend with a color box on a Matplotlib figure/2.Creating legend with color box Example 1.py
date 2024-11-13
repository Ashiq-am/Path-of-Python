# Import libraries
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Creating plot
plt.plot([1, 2, 3, 4], color='blue')

plt.title('simple legend example ')

# Creating legend with color box
blue_patch = mpatches.Patch(color='blue', label='blue legend')
plt.legend(handles=[blue_patch])

# Show plot
plt.show()
