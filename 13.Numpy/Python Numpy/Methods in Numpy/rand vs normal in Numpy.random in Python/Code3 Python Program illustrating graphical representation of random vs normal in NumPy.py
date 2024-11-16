# Python Program illustrating
# graphical representation of
# numpy.random.normal() method
# numpy.random.rand() method

import numpy as geek
import matplotlib.pyplot as plot

# 1D Array as per Gaussian Distribution
mean = 0
std = 0.1
array = geek.random.normal(0, 0.1, 1000)
print("1D Array filled with random values "
	"as per gaussian distribution : \n", array);

# Source Code :
# https://docs.scipy.org/doc/numpy-1.13.0/reference/
# generated/numpy-random-normal-1.py
count, bins, ignored = plot.hist(array, 30, normed=True)
plot.plot(bins, 1/(std * geek.sqrt(2 * geek.pi)) *
		geek.exp( - (bins - mean)**2 / (2 * std**2) ),
		linewidth=2, color='r')
plot.show()


# 1D Array constructed Randomly
random_array = geek.random.rand(5)
print("1D Array filled with random values : \n", random_array)

plot.plot(random_array)
plot.show()
