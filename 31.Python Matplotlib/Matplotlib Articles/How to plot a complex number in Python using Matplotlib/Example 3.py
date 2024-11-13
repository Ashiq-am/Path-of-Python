# import libraries
import matplotlib.pyplot as plt
import numpy as np

# create data of complex numbers using numpy
data = np.arange(8) + 1j*np.arange(-4, 4)

# extract real part using numpy
x = data.real
# extract imaginary part using numpy
y = data.imag

# plot the complex numbers
plt.plot(x, y, '-.r*')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()
