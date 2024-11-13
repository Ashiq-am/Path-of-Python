# import packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(-10, 10, 20)
y = x

# plot the graph
plt.plot(x, y)

# limited to show positive axes
plt.xlim(0)
plt.ylim(0)
