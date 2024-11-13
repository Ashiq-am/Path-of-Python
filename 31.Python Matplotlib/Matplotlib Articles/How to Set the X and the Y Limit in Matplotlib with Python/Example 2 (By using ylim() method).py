# import packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(-10, 10, 1000)
y = np.cos(x)

# plot the graph
plt.plot(x, y)

# limit y by 0 to 1
plt.ylim(0, 1)
