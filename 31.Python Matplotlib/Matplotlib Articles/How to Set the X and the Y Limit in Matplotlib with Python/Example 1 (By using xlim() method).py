# import packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(-10, 10, 1000)
y = np.sin(x)

# plot the graph
plt.plot(x, y)

# limit x by -5 to 5
plt.xlim(-5, 5)
