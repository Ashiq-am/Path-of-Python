# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
y2 = y + 0.2 * np.random.normal(size=x.shape)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y2)

ax.set_xticks([0, np.pi, 2 * np.pi])
ax.set_xticklabels(['0', r'$pi$', r'2$pi$'])

ax.spines['left'].set_bounds(-1, 1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

w = ax.get_xmajorticklabels()
# print(list(w))
strr = str(list(w))
ax.text(2, 0, "xmajorticklabels values : ",
        fontweight="bold")
ax.text(1, -0.2, strr, fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_xmajorticklabels()\
function Example\n\n', fontweight="bold")
fig.canvas.draw()
plt.show()
