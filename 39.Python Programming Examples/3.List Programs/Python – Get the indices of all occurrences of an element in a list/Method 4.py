# import numpy module
import numpy

# initialize a array
my_list = numpy.array([1, 2, 3, 1, 5, 4])
indices = numpy.where(my_list == 1)[0]

# display result
print(indices)
