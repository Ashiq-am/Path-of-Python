# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y1 = -3 * x * x + 10 * x + 10
y2 = 3 * x * x + x

fig, ax = plt.subplots()
ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2 > y1,
                facecolor='green', alpha=0.8)
ax.fill_between(x, y1, y2, where=y2 <= y1,facecolor = "black", alpha = 0.8)

x = ax.get_facecolor()
ax.text(-2, 80, "Value of facecolor : " + str(x),
        style='italic', fontsize=10,
        color="green")
ax.set_title('matplotlib.axes.Axes.get_facecolor()\
Example\n', fontsize=12, fontweight='bold')
plt.show()
