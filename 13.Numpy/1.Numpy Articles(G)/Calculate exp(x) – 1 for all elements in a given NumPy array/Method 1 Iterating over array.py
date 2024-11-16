# importing numpy
import numpy


arr = [1, 2, 3, 4]

print("Input : ", arr)
for i in range(len(arr)):
	arr[i] = numpy.exp(arr[i])-1

print("Output : ", arr)

arr = [3, 0.3, 3.1, 2.2]

print("Input : ", arr)
for i in range(len(arr)):
	arr[i] = numpy.exp(arr[i])-1

print("Output : ", arr)
