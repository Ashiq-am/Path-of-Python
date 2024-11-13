import numpy

# create a simple array with numpy empty()
a = numpy.empty(5, dtype=object)
print(a)

# create multi-dim array by providing shape
matrix = numpy.empty(shape=(2,5),dtype='object')
print(matrix)
