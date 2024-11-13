# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

fig, ax = plt.subplots()

ax.stem(x, y, linefmt ='grey',
		markerfmt ='D',
		bottom = 1.1,
		use_line_collection = True)

ax.set_title('matplotlib.axes.Axes.stem Example')
plt.show()
