# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt

# providing values to x and y
x = [8, 5, 11, 13, 16, 23]
y = [14, 8, 21, 7, 12, 15]

# to plot x and y
plt.plot(x, y)

# use of axes() property
axs = Artist.axes
plt.text(8.5, 14, str(axs), fontweight="bold")

plt.title("""matplotlib.artist.Artist.axes() 
property Example""", fontweight="bold")

plt.show()
