# Python code to demonstrate the
# use of numpy.frompyfunc
import numpy as np

# create an array of numners
a = np.array([34, 67, 89, 15, 33, 27])

# python str function as ufunc
string_generator = np.frompyfunc(str, 1, 1)

print("Original array-", a)
print("After conversion to string-", string_generator(a))
