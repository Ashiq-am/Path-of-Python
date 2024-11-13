# importing poisson fro scipy
from scipy.stats import poisson

# importing nupy as np
import numpy as np

# importing matplotlib as plt
import matplotlib.pyplot as plt


# creating a numy array for x-axis
# using step size as 1
x = np.arange(0, 100, 1)

# poisson distribution data for y-axis
y = poisson.pmf(x, mu=10, loc=40)


# plotting the graph
plt.plot(x, y)

# showing the graph
plt.show()
