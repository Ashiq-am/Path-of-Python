# import packkages
import numpy as np
import matplotlib.pyplot as plt

# create data
A = np.array([3,6,9,4,2,5])
B = np.array([2,8,1,9,7,3])
X = np.arange(6)

# plot the bars
plt.barh(X, A, align='center',
		alpha=0.9, color = 'y')

plt.barh(X, -B, align='center',
		alpha=0.6, color = 'c')

plt.grid()
plt.title("Back-to-Back Bar Chart")
plt.ylabel("Indexes")
plt.xlabel("Values")
plt.show()
