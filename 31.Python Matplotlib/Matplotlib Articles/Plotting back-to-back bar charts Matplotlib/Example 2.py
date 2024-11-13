# import packkages
import numpy as np
import matplotlib.pyplot as plt

# create data
A = np.array([3,6,9,4,2,5])
B = np.array([2,8,1,9,7,3])
X = np.arange(6)

# plot the bars
plt.barh(X, A, color = 'r')
plt.barh(X, -B, color = 'b')
plt.title("Back-to-Back Bar Chart")
plt.show()
