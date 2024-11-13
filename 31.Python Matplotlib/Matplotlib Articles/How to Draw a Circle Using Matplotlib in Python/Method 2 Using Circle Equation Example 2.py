# Program to plot a Circle
# using Center-Radius form of circle equation

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace( -0.7 , 0.7 , 150 )
y = np.linspace( -0.7 , 0.7 , 150 )

a, b = np.meshgrid( x , y )

C = a ** 2 + b ** 2 - 0.2

figure, axes = plt.subplots()

axes.contour( a , b , C , [0] )
axes.set_aspect( 1 )

plt.title( 'Center-Radius form Circle' )
plt.show()
