# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.cm as cm

from matplotlib.collections import LineCollection
from matplotlib.ticker import MultipleLocator

with cbook.get_sample_data('s1045.ima.gz') as dfile:
	im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))

im = np.ravel(im)
im = im[np.nonzero(im)]
im = im / (2**20 - 1)
plt.hist(im, bins = 40, color ="green")

plt.minorticks_on()
plt.title('matplotlib.pyplot.minorticks_on() function Example', fontweight ="bold")
plt.show()
