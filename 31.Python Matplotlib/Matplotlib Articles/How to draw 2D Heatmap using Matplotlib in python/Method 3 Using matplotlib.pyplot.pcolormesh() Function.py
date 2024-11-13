# Program to plot 2-D Heat map
# using matplotlib.pyplot.pcolormesh() method
import matplotlib.pyplot as plt
import numpy as np

Z = np.random.rand( 15 , 15 )

plt.pcolormesh( Z , cmap = 'summer' )

plt.title( '2-D Heat Map' )
plt.show()
