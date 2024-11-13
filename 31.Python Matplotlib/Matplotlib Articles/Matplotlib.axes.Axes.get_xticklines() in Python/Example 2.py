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

w = ax.get_xticklines()
ax.text(2, 0.8, "xticklines values : ",
        fontweight="bold")
xx = 0.8
for i in w:
    ax.text(2.3, xx - 0.2, str(i), fontweight="bold")
    xx -= 0.2

fig.suptitle('matplotlib.axes.Axes.get_xticklines() \
function Example\n\n', fontweight="bold")
fig.canvas.draw()
plt.show()
