# Import libraries
from matplotlib import pyplot as plt
import numpy as np

# Creating dataset
l = np.random.randint(150)

# Creating plot
plt.hist(l, bins=l,
		color='lime')

# show plot
plt.show()
