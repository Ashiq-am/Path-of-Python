# In this program we are demonstraiting how wrong
# input course invalid value
# encountered in double_scalars
import numpy

array1 = [1, 2, 4, 7, 8]

# this input array couses error
array2 = []

Marray1 = numpy.mean(array1)
# this line couses the error
Marray2 = numpy.mean(array2)


print(Marray1)
print(Marray2)
