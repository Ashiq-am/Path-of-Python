from matplotlib.widgets import MultiCursor
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

x1 = ['Telugu', 'Hindi', 'English',
	'Maths', 'Science', 'Social']
y1 = [45, 34, 30, 45, 50, 38]
y2 = [36, 28, 30, 45, 38, 50]

labels = ["in 2020", "in 2021"]

l1 = ax1.plot(x1, y1, 'o', color="green")
l2 = ax2.plot(x1, y2, 'o', color="blue")

ax1.set_yticks(np.arange(0, 51, 5))
ax2.set_yticks(np.arange(0, 51, 5))

ax1.set_ylabel('Number of students passed', fontsize=15)

fig.legend([l1, l2], labels=labels, loc="upper right")
cursor = MultiCursor(fig.canvas, (ax1, ax2), color='r',
					lw=2, horizOn=True, vertOn=True)

plt.subplots_adjust(right=0.9)
plt.show()
