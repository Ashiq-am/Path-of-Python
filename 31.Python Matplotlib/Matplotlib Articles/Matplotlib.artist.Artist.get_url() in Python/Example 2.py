# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

f, ax = plt.subplots()
delta = 0.025

x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2

ax.imshow(Z, interpolation='bilinear',
          cmap="PuBuGn_r",
          origin='lower',
          extent=[-3, 3, -3, 3])

ax.set_url('https://www.geeksforgeeks.org/')
f.savefig('image.svg')

ax.set_title("URL : " + str(Artist.get_url(ax)), fontweight="bold")

f.suptitle("""matplotlib.artist.Artist.get_url() 
function Example""", fontweight="bold")

plt.show()
