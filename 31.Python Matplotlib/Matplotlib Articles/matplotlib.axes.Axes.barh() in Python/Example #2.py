# ImpleMinetation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

labels = ['Month1', 'Month2',
		'Month3', 'Month4']

mine = [21, 52, 33, 54]
others = [54, 23, 32, 41]
Mine_std = [2, 3, 4, 1]
Others_std = [3, 5, 2, 3]
width = 0.3

fig, ax = plt.subplots()

ax.barh(labels, mine, width,
		xerr = Mine_std,
		label ='Mine')

ax.barh(labels, others, width,
		xerr = Others_std,
		left = mine,
		label ='Others')

ax.set_xlabel('Articles')
ax.legend()

ax.set_title('matplotlib.axes.Axes.barh Example')

plt.show()
