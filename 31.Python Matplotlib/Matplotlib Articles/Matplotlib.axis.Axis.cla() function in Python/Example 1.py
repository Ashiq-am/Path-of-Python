# Implementation of matplotlib function
from matplotlib.axis import Axis
from matplotlib.artist import Artist
import matplotlib.pyplot as plt

# providing values to x and y
x = [8, 5, 11, 13, 16, 23]
y = [14, 8, 21, 7, 12, 15]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

Axis.cla(ax.xaxis)
Axis.cla(ax.yaxis)

plt.title("Matplotlib.axis.Axis.cla()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
