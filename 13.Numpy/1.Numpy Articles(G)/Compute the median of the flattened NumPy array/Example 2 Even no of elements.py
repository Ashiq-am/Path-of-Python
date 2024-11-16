# importing numpy as library
import numpy as np


# creating 1 D array with even no of
# elements
x_even = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("\nPrinting the Original array:")
print(x_even)

# calculating median
med_even = np.median(x_even)
print("\nMedian of the array that contains even no of elements:")
print(med_even)
