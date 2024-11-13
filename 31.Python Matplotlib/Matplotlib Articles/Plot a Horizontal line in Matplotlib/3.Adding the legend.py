# importing the module
import matplotlib.pyplot as plt

# plotting line within the given range
plt.axhline(y=.5, xmin=0.25, xmax=0.9)

# line colour is blue
plt.axhline(y=3, color='b', linestyle=':', label="blue line")

# line colour is white
plt.axhline(y=1, color='w', linestyle='--', label="white line")

# line colour is red
plt.axhline(y=2, color='r', linestyle='dashed', label="red line")

# adding axis labels
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# plotting the legend
plt.legend(bbox_to_anchor=(1.0, 1), loc='upper center')

# displaying the plot
plt.show()
