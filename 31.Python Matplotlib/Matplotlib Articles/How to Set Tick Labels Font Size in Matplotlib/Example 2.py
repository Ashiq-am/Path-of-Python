# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = list(range(1, 11, 1))
y = np.log(x)

# make objects of subplots
fig, ax = plt.subplots()

# plot the data
ax.plot(x, y)

# change the fontsize
ax.set_xticklabels(x, fontsize=20)

# show the plot
plt.show()
