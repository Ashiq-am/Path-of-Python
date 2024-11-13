# Python Program illustrating
# pyplot.colorbar() method
import numpy as np
import matplotlib.pyplot as plt

# Dataset
# List of total number of items purchased
# from each products
purchaseCount = [100, 200, 150, 23, 30, 50,
				156, 32, 67, 89]

# List of total likes of 10 products
likes = [50, 70, 100, 10, 10, 34, 56, 18, 35, 45]

# List of Like/Dislike ratio of 10 products
ratio = [1, 0.53, 2, 0.76, 0.5, 2.125, 0.56,
		1.28, 1.09, 1.02]

# scatterplot
plt.scatter(x=purchaseCount, y=likes, c=ratio, cmap="summer")

plt.colorbar(label="Like/Dislike Ratio", orientation="horizontal")
plt.show()
