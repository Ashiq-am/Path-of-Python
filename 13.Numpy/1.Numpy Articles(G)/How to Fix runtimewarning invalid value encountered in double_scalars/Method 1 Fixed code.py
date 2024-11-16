import numpy

array1 = [1, 2, 4, 7, 8]

# this input array couses error
array2 = []

# Here we check error
if array1 and array2:
	print("Mean of the array 1 is : ", numpy.mean(array1))
	print("Mean of the array is :", numpy.mean(array2))
else:
	print("please Enter valid array")
