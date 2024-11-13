# libraries
import sample
import array
import numpy

print("Average of list : ", sample.avg([1, 2, 3]))

print("\nAverage of tuple : ", sample.avg((1, 2, 3)))

print("\nAverage of array : ", sample.avg(array.array('d', [1, 2, 3])))

print("\nAverage of numpy array : ", sample.avg(numpy.array([1.0, 2.0, 3.0])))
