#Python 3 code to flatten nested list
#Contributed by S Lakshman Rao - kaapalx
import numpy

ini_list=[[1, 2, 3],
		[3, 6, 7],
		[7 ,5, 4]]

print("Initial list ",ini_list) #Printing Initial list

print("Flattened List ",list(numpy.concatenate(ini_list).flat))
#Using numpy to flatten list and printing the result
