# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y1 = -3 * x * x + 10 * x + 10
y2 = 3 * x * x + x

fig, ax = plt.subplots()
fig.tight_layout()
ax.plot(x, y1, x, y2, color='black')

ax.fill_between(x, y1, y2,
                where=y2 > y1,
                facecolor='green',
                alpha=0.8)

ax.fill_between(x, y1, y2,
                where=y2 <= y1,
                facecolor='black',
                alpha=0.8)

fig.set_tight_layout(True)

fig.canvas.draw()

fig.suptitle("""matplotlib.figure.Figure.set_tight_layout() 
function Example\n\n""", fontweight="bold")

plt.show()
