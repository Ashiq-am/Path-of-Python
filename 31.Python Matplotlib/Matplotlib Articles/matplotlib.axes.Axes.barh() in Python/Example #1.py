# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

data = ((1000, 30), (30, 10),
		(30, 100), (800, 500),
		(50, 10))

dim = len(data[0])
w = 0.3
dimw = w / dim

fig, ax = plt.subplots()
x = np.arange(len(data))

for i in range(len(data[0])):
	y = [d[i] for d in data]
	b = ax.barh(x + i * dimw, y,
				dimw, left = 0.001)

ax.set_yticks(x + dimw / 2)
ax.set_yticklabels(map(str, x))
ax.set_xscale('log')

ax.set_title('matplotlib.axes.Axes.barh Example')

plt.show()
