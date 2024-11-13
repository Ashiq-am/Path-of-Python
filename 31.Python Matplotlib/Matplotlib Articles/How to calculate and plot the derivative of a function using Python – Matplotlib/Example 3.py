# importing modules
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np

# method to return function
def function(x):
	return 4*x**2+x+1

# method to return its derivative
def deriv(x):
	return derivative(function, x)

#range in x-axis
y = np.linspace(-6, 6)

# plotting function
plt.plot(y, function(y), color='brown', label='Function')

# plotting its derivative
plt.plot(y, deriv(y), color='blue', label='Derivative')

# changing limits of y-axis
plt.gca().spines['left'].set_position('zero',)

# changing limits of x-axis
plt.gca().spines['bottom'].set_position('zero',)
plt.legend(loc='upper left')

# plotting text in the graph
plt.text(5.0, 1.0, r"$f'(x)=8x+1$", horizontalalignment='center',
		fontsize=18, color='blue')

plt.text(-4.4, 25.0, r'$f(x)=4x^2+x+1$', horizontalalignment='center',
		fontsize=18, color='brown')
plt.grid(True)
