import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_ylim(1, 0)
ax.set_ylabel('Display Y-axis Label', fontweight='bold')
ax.grid(True)

w = ax.get_ylabel()
ax.set_ylabel("")
ax.text(1.5, 0.58, "Previously assigned Y-Label : \n\n" + str(w),
        fontsize=12)
fig.suptitle("matplotlib.axes.Axes.get_ylabel() function\
Example\n", fontweight="bold")
plt.show()
