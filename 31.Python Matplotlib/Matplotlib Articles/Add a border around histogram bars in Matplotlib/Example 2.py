# importing package
from matplotlib import pyplot as plt
import numpy as np

#create data
fig,ax = plt.subplots(1, 1)

a = np.array([20, 73, 55, 31, 51, 5, 79, 5,
			43, 22, 87, 54, 11, 56, 27])

b = np.array([0, 25, 50, 75, 100])

# Adjust the border color
ax.hist(a, edgecolor = "black", color = 'pink')
ax.hist(b, edgecolor = "red", color = 'gray')

ax.set_title("Histogram - Geekforgeeks")
plt.show()
