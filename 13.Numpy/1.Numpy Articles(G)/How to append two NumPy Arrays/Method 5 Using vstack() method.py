import numpy


array1 = numpy.array([1, 2, 3, 4, 5])
array2 = numpy.array([6, 7, 8, 9, 10])

# Stack arrays in sequence vertically (row wise).
array1 = numpy.vstack([array1, array2])
print(array1)
