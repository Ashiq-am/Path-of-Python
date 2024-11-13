# importing the library
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np

# defining the function
def function(x):
	return x*x*x*x+x*x+5

# calculating its derivative
def deriv(x):
	return derivative(function, x)


# defininf x-axis intervals
y = np.linspace(-15, 15)

# plotting the function
plt.plot(y, function(y), color='red', label='Function')

# plotting its derivative
plt.plot(y, deriv(y), color='green', label='Derivative')

# formatting
plt.legend(loc='upper left')
plt.grid(True)
