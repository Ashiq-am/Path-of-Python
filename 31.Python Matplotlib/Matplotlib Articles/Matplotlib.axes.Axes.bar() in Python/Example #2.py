# ImpleMinetation of matplotlib function


import numpy as np
import matplotlib.pyplot as plt

labels = ['Month1', 'Month2', 'Month3', 'Month4']
mine = [21, 52, 33, 54]
others = [54, 23, 32, 41]
Mine_std = [2, 3, 4, 1]
Others_std = [3, 5, 2, 3]
width = 0.3

fig, ax = plt.subplots()

ax.bar(labels, mine, width,
       yerr=Mine_std,
       label='Mine')

ax.bar(labels, others, width,
       yerr=Others_std,
       bottom=mine,
       label='Others')

ax.set_ylabel('Articles')
ax.legend()

ax.set_title('matplotlib.axes.Axes.bar Example')

plt.show()
