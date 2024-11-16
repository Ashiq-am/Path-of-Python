# Python code to demonstrate bitwise-function
import numpy as np

# construct an array of even and odd numbers
even = np.array([0, 2, 4, 6, 8, 16, 32])
odd = np.array([1, 3, 5, 7, 9, 17, 33])

# bitwise_and
print('bitwise_and of two arrays: ')
print(np.bitwise_and(even, odd))

# bitwise_or
print('bitwise_or of two arrays: ')
print(np.bitwise_or(even, odd))

# bitwise_xor
print('bitwise_xor of two arrays: ')
print(np.bitwise_xor(even, odd))

# invert or not
print('inversion of even no. array: ')
print(np.invert(even))

# left_shift
print('left_shift of even no. array: ')
print(np.left_shift(even, 1))

# right_shift
print('right_shift of even no. array: ')
print(np.right_shift(even, 1))
