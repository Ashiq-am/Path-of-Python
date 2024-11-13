# array module example
import work
import array
import numpy

arr = array.array('d', [1, -3, 4, 7, 2, 0])
print ("Array : ", arr)

# Clipping the array
work.clip(arr, 1, 4, arr)
print ("\nClipping array : ", arr)

# numpy example
arr2 = numpy.random.uniform(-10, 10, size = 1000000)
print ("\narr2 : \n", arr2)

arr3 = numpy.zeros_like(arr2)
print ("\narr3 : \n", arr3)

work.clip(arr2, -5, 5, arr3)
print ("\nClipping arr3 : \n", ar3)
print ("\nMinimum in arr3 : ", min(arr3))
print ("\nMaximum in arr3 : ", min(arr3))
