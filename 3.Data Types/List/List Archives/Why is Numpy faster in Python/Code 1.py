# importing required packages
import numpy
import time

# size of arrays and lists
size = 1000000

# declaring lists
list1 = range(size)
list2 = range(size)

# declaring arrays
array1 = numpy.arange(size)
array2 = numpy.arange(size)

# list
initialTime = time.time()
resultantList = [(a * b) for a, b in zip(list1, list2)]

# calculating execution time
print("Time taken by Lists :",
	(time.time() - initialTime),
	"seconds")

# NumPy array
initialTime = time.time()
resultantArray = array1 * array2

# calculating execution time
print("Time taken by NumPy Arrays :",
	(time.time() - initialTime),
	"seconds")
