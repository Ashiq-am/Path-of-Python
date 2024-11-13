import numpy as np
import matplotlib.pyplot as plt

# X-axis values
x = np.arange(5)

# Y-axis values
y1 = [1, 2, 3, 4, 5]

# Y-axis values
y2 = [1, 4, 9, 16, 25]

# Function to plot
plt.plot(x, y1, label ='Numbers')
plt.plot(x, y2, label ='Square of numbers')

# Function add a legend
plt.legend()

# function to show the plot
plt.show()
