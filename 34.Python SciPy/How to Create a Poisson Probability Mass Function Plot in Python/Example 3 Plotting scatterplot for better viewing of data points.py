# importing poisson fro scipy
from scipy.stats import poisson

# importing nupy as np
import numpy as np

# importing matplotlib as plt
import matplotlib.pyplot as plt


# creating a numy array for x-axis
x = np.arange(0, 100, 0.5)

# poisson distribution data for y-axis
y = poisson.pmf(x, mu=50, loc=0)


# plotting thescatter plot graph
plt.scatter(x, y)

# showing the graph
plt.show()
