# import the numpy module
import numpy

# import chebyshev
from numpy.polynomial import chebyshev

# create array of coefficients with
# 6 elements each
first = numpy.array([6, 7, 5])
second = numpy.array([4, 5, 6])

# Display the coefficient arrays
print(f"First array: {first} \nSecond array: {second}")

# get the shape, # get the dimensions
print(f"\nShape of First array: {first.shape} Dimension: {first.ndim}")
print(f"Shape of second array: {second.shape} Dimension: {second.ndim}")


# multiply two chebyshev series.
print("Product of two chebyshev series: ",chebyshev.chebmul(first,second))
