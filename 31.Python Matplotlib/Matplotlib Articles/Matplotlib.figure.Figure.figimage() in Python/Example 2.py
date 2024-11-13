# Implementation of matplotlib function
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo = 500, yo = 100,
				origin ='lower')

im2 = fig.figimage(Z, xo = 100, yo = 100,
				alpha =.6,
				origin ='lower')

fig.suptitle('matplotlib.figure.Figure.figimage() function Example', fontweight ="bold")

plt.show()
