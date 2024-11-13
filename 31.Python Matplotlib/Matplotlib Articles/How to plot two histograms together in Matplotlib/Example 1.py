# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# generating two series of random
# values using numpy random module
# of shape (500,1)
series1 = np.random.randn(500, 1)
series2 = np.random.randn(400, 1)

# plotting first histogram
plt.hist(series1)

# plotting second histogram
plt.hist(series2)

# Showing the plot using plt.show()
plt.show()
