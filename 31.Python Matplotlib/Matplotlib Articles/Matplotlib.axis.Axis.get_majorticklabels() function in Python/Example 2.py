# Implementation of matplotlib function
from matplotlib.axis import Axis
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n = 100000
x = np.random.standard_normal(n)
y = 2 * np.random.standard_normal(n)
z = [1, 2, 3, 4]

xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

fig, ax = plt.subplots()
hb = ax.hexbin(x, y,
               gridsize=50,
               bins='log',
               cmap='BuGn')

ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
ax.xaxis.set_ticklabels(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
print("Value of get_majorticklabels() :")
for i in ax.xaxis.get_majorticklabels():
    print(i)

plt.title("Matplotlib.axis.Axis.get_majorticklabels()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
