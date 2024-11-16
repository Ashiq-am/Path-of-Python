# importing the module
import numpy as np

# creating a NumPy array
complex_num = np.array([-1, 31, 0.5])

# traversing the list
for i in range(len(complex_num)):
	print("{}. Number is {}".format(i + 1, complex_num[i]))
	print ("The real part is: {}".format(complex_num[i].real))
	print ("The imaginary part is: {}\n".format(complex_num[i].imag))
