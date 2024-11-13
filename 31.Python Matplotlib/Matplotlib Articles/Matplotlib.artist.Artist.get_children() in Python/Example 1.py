# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax2 = plt.subplots()

art = ax2.bar(range(10), rand(10), picker=True)

print("List of the child Artists of this Artist \n",
      *list(art.get_children()), sep="\n")

plt.title("""matplotlib.artist.Artist.get_children() 
function Example""", fontweight="bold")

plt.show()
