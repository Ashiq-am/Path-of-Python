import numpy


array1 = numpy.array([1, 2, 3, 4, 5])
array2 = numpy.array([6, 7, 8, 9, 10])

# Appending both Arrays using concatenate() method.
array1 = numpy.concatenate([array1, array2])
print(array1)
