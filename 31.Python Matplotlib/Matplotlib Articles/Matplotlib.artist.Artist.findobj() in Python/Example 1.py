# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax2 = plt.subplots()

ax2.bar(range(10), rand(10), picker=True)

print("Value return : \n",
      *list(Artist.findobj(ax2)), sep="\n")

plt.title("""matplotlib.artist.Artist.findobj() 
function Example""", fontweight="bold")

plt.show()
