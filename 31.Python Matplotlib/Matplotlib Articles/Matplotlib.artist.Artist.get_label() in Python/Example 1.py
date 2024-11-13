# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [0, 1]
y = [1, 1]
line, = ax.plot(x, y)

ax.legend(("Line_1",))

ax.text(0.2, 1.02, "Value Return by get_label()\
: " + str(Artist.get_label(line)))

fig.suptitle("""matplotlib.artist.Artist.get_label() 
function Example""", fontweight="bold")

plt.show()
