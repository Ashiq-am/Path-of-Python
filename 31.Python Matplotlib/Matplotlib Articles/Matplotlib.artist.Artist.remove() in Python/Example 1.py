# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt


fig, axs = plt.subplots()
axs.plot([1, 2, 3])

# use of remove() method
Artist.remove(axs)

fig.suptitle("""matplotlib.artist.Artist.remove() 
function Example""", fontweight="bold")

plt.show()
