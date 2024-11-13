# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])

axs.set_title("Is artist is explicitly set transform : "
              + str(Artist.is_transform_set(axs)))

fig.suptitle("""matplotlib.artist.Artist.is_transform_set() 
function Example""", fontweight="bold")

plt.show()
