# importing package
import matplotlib.pyplot as plt
import numpy as np

# create data
X = [1, 2, 3, 4, 5]
Y = [3, 3, 3, 3, 3]

# plot lines
plt.plot(X, Y, label = "Line-1")
plt.plot(Y, X, label = "Line-2")
plt.plot(X, np.sin(X), label = "Curve-1")
plt.plot(X, np.cos(X), label = "Curve-2")

# Change the label spacing here
plt.legend(labelspacing = 3)
plt.title("Line Graph - Geeksforgeeks")

plt.show()
