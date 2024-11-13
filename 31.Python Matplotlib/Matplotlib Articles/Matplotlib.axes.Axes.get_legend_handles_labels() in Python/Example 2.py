# Implementation of matplotlib function
import numpy as np

np.random.seed(19680801)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for color in ['tab:green', 'tab:blue', 'tab:orange']:
    n = 70
    x, y = np.random.rand(2, n)
    scale = 1000.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.35)

ax.legend()
ax.grid(True)

h, l = ax.get_legend_handles_labels()
print(h, l)
text = " Legend is present"
if h == []:
    text = "No legend present"
else:
    text += " and labels are : \n" + str(l)

ax.text(0.15, 0.45, text, fontweight="bold")
fig.suptitle('matplotlib.axes.Axes.get_legend_handles_labels()\
function Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()
