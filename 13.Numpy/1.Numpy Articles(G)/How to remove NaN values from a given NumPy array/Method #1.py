import numpy


# create a 1D array
a = numpy.array([5, 2, 8, 9, 3, numpy.nan,
				2, 6, 1, numpy.nan])

# remove nan values using numpy.isnan()
# and numpy.logical_not
b = a[numpy.logical_not(numpy.isnan(a))]

# print the results
print("original 1D array				 ->", a)
print("1D array after removing nan values ->", b)
print()

# create a 2D array
c = numpy.array([[6, 2, numpy.nan], [2, 6, 1],
				[numpy.nan, 1, numpy.nan]])

# remove nan values using numpy.isnan()
# and numpy.logical_not
d = c[numpy.logical_not(numpy.isnan(c))]

# print the results
print("Original 2D array ->")
print(c)
print("2D array converted to 1D after removing nan values ", d)
