# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)],
			(10, 9),
			facecolors ='tab:green')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)

ax.set_title('matplotlib.axes.Axes.broken_barh Example')
plt.show()
