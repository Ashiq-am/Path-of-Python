# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt

f, ax = plt.subplots()
ax.scatter([1, 2, 3], [4, 5, 6])
ax.set_url('http://www.google.com')
f.canvas.print_figure('scatter.svg')

ax.text(1.5, 5.5, "URL : "
        + str(Artist.get_url(ax)),
        fontweight="bold")

f.suptitle("""matplotlib.artist.Artist.get_url() 
function Example""", fontweight="bold")

plt.show()
