import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

x1 = [1, 2, 3, 4, 5, 6]
y1 = [45, 34, 30, 45, 50, 38]
y2 = [36, 28, 30, 40, 38, 48]

labels = ["student 1", "student 2"]

fig.suptitle(' Student marks in different subjects ', fontsize=30)

# Creating the sub-plots.
l1 = ax1.plot(x1, y1, 'o-', color='g')
l2 = ax2.plot(x1, y2, 'o-')

fig.legend([l1, l2], labels=labels,
		loc="upper right")
plt.subplots_adjust(right=0.9)

plt.show()
