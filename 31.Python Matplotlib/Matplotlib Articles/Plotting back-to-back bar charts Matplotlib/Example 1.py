# import packkages
import numpy as np
import matplotlib.pyplot as plt

# create data
A = np.array([3,6,9,4,2,5])
X = np.arange(6)

# plot the bars
plt.bar(X, A, color = 'r')
plt.bar(X, -A, color = 'b')
plt.title("Back-to-Back Bar Chart")
plt.show()
