# importing packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.linspace(-5, 5, 1000)
colors = [['c', 'g'], ['y', 'r']]

# make subplot and plots the grpahs
fig, ax = plt.subplots(2, 2)
for i in range(2):
    ax[0][i].plot(x, np.sin(x + i),
                  color=colors[0][i],
                  label="y=sin(x+{})".format(i))

    ax[1][i].plot(x, np.sin(x + i),
                  color=colors[1][i],
                  label="y=sin(x+{})".format(i))

# set legend position
fig.legend(bbox_to_anchor=(1.3, 0.6))

# set spacing to subplots
fig.tight_layout()
plt.show()
