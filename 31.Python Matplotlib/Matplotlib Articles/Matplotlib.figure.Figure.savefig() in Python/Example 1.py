# Implementation of matplotlib function
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
s = ax.scatter([1, 2, 3], [4, 5, 6])
s.set_url('http://www.google.com')

fig.savefig('scatter.svg')

fig.suptitle("""matplotlib.figure.Figure.savefig() 
function Example\n\n""", fontweight="bold")

plt.show()
