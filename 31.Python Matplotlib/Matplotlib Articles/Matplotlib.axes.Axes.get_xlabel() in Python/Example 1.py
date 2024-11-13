import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)
ax.set_xlabel('Display X-axis Label', fontweight ='bold')
ax.grid(True)

w = ax.get_xlabel()
ax.set_xlabel("")
ax.text(3.5, 0.5, "Previously assigned X-Label : \n\n"+str(w),
		fontsize = 12)
fig.suptitle("matplotlib.axes.Axes.get_xlabel() function Example\n", fontweight ="bold")
plt.show()
