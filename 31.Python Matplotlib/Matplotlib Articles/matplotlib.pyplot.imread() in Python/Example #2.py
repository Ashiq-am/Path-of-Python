# Implementation of matplotlib function
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt


with cbook.get_sample_data('loggf.png') as file:
	im = image.imread(file)

fig, ax = plt.subplots()

ax.plot(np.cos(10 * np.linspace(0, 1)), '-o', ms = 15,
							alpha = 0.6, mfc ='green')

ax.grid()
fig.figimage(im, 10, 10, zorder = 3, alpha =.5)

plt.title('matplotlib.pyplot.imread() function Example',
									fontweight ="bold")
plt.show()
