# importing package
import matplotlib.pyplot as plt
import numpy as np

# create data
X = [1, 2, 3, 4, 5]

# plot lines
plt.plot(X, np.sin(X), label = "Curve-1")
plt.plot(X, np.cos(X), label = "Curve-2")

# Add a title to a legend
plt.legend(title = "Legend Title")
plt.title("Line Graph - Geeksforgeeks")

plt.show()
