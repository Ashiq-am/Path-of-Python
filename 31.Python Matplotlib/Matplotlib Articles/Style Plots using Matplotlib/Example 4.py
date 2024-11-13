# importing all the necessary packages
import numpy as np
import matplotlib.pyplot as plt

# importing the style package
from matplotlib import style

with plt.style.context('dark_background'):
	plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')

plt.show()
