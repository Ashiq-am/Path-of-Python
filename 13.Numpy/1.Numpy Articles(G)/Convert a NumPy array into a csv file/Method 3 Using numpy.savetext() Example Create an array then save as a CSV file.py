# import numpy library
import numpy

# create an array
a = numpy.array([[1, 6, 4],
				[2, 4, 8],
				[3, 9, 1]])

# save array into csv file
numpy.savetxt("data3.csv", a,delimiter = ",")
