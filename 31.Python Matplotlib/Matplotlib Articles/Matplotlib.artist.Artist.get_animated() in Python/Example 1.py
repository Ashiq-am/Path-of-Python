# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.array([[1, 2, 3, 4, 5],
                 [7, 4, 9, 2, 3]])

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

line, = ax.plot([], [], 'r-')
annotation = ax.annotate('', xy=(data[0][0],
                                 data[1][0]))

Artist.set_animated(annotation, True)
w = Artist.get_animated(annotation)

print(str(w))

fig.suptitle('matplotlib.artist.Artist.get_animated()\
function Example', fontweight="bold")

ax.grid()

plt.show()
