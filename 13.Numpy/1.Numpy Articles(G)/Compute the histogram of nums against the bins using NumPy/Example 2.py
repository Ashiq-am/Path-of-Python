# Import libraries
from matplotlib import pyplot as plt
import numpy as np

# Creating dataset
l = [i for i in range(50)]

# Creating plot
plt.hist(l, bins=[1, 2, 3, 4, 5],
		color='green')

# show plot
plt.show()
