# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt

# providing values to x and y
x = [8, 5, 11, 13, 16, 23]
y = [14, 8, 21, 7, 12, 15]

# to plot x and y
plt.plot(x, y)
plt.axes(facecolor='black')

axs = Artist.axes
print(str(axs))

plt.title("""matplotlib.artist.Artist.axes() 
property Example""", fontweight="bold")

plt.show()
