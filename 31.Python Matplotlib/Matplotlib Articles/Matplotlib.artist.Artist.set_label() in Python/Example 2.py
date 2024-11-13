# Implementation of matplotlib function
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
               cmap='PuBuGn')

ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

cb = fig.colorbar(hb, ax=ax)
cb.set_label('log')

fig.suptitle("""matplotlib.artist.Artist.set_label() 
function Example""", fontweight="bold")

plt.show()
