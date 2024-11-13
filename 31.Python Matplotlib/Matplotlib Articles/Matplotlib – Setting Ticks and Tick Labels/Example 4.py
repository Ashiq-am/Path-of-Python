# import required modules
import matplotlib.pyplot as plt
import numpy as np
import math

# assign coordinates
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
ax = plt.axes()
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# depict illustration
plt.plot(x, y, color="lime")

# setting ticks for x-axis
ax.set_xticks([0, 2, 4, 6])

# setting ticks for y-axis
ax.set_yticks([-1, 0, 1])

# setting label for y tick
ax.set_yticklabels(["sin(-90deg)", "sin(0deg)", "sin(90deg)"])

plt.show()
