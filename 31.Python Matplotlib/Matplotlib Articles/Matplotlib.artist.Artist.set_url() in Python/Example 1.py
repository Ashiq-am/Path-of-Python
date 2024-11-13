# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f, ax = plt.subplots()
s = ax.scatter([1, 2, 3], [4, 5, 6])
Artist.set_url(s, 'http://www.google.com')
f.canvas.print_figure('geeks1.svg')

f.suptitle("""matplotlib.artist.Artist.set_url() 
function Example""", fontweight="bold")

plt.show()
