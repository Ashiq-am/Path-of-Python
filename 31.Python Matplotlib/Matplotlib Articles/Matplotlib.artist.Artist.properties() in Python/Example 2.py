# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)
geeks = np.random.randn(100)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines=True,
         normed=True,
         maxlags=80, lw=3)

ax.grid(True)

w = Artist.properties(ax)
print("Display all Properties\n")
for i in w:
    print(i, ":", w[i])

fig.suptitle('matplotlib.artist.Artist.properties() \
function Example', fontweight="bold")

plt.show()
