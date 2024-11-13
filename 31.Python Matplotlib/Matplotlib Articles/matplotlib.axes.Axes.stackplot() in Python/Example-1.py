# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

y = np.vstack([y1, y2, y3])

labels = ["Geeks1 ", "Geeks2", "Geeks3"]

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3,
			labels = labels)

ax.legend(loc ='upper left')

ax.set_title('matplotlib.axes.Axes.stackplot Example')
plt.show()
