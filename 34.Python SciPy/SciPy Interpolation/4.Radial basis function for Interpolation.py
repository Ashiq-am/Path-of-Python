# Import the required libraries
import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

# setup the data values
x = np.linspace(0, 10, 9)
y = np.cos(x/2)
xi = np.linspace(0, 10, 110)

# Interpolation using RBF
rbf = Rbf(x, y)
fi = rbf(xi)

plt.subplot(2, 1, 2)
plt.plot(x, y, '*', color="green")
plt.plot(xi, fi, 'green')
plt.plot(xi, np.sin(xi), 'black')
plt.title('Radial basis function Interpolation')
plt.show()
