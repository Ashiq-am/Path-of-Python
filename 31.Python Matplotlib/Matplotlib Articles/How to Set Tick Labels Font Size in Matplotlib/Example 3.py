# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = list(range(1, 11, 1))
y = np.sin(x)

# make objects of subplots
fig, ax = plt.subplots(1, 1)

# plot the data
ax.plot(x, y)

# change the fontsize
ax.tick_params(axis='x', labelsize=20)

# show the plot
plt.show()
