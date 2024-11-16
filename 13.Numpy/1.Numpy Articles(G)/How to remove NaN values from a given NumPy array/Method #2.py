import numpy


# create a 2D array
c = numpy.array([[12, 5, numpy.nan, 7],
				[2, 61, 1, numpy.nan],
				[numpy.nan, 1,
				numpy.nan, 5]])

# remove nan values using numpy.isnan()
# and numpy.logical_not
d = c[~(numpy.isnan(c))]

# print the results
print("Original 2D array ")
print(c)
print()

print("2D array converted to 1D after removing nan values ")
print(d)
