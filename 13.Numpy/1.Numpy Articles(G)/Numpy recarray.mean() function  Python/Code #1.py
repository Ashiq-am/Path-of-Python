# Python program explaining
# numpy.recarray.mean() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(5.0, 2), (3.0, 6), (6.0, 10)],
					[(9.0, 1), (5.0, 4), (-12.0, 7)]],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.mean methods
# to float record array along default axis
# i, e along flattened array
out_arr1 = rec_arr.a.mean()
# Mean of the flattened array
print("\nMean of float record array, axis = None : ", out_arr1)


# applying recarray.mean methods
# to float record array along axis 0
# i, e along vertical
out_arr2 = rec_arr.a.mean(axis = 0)
# Mean along 0 axis
print("\nMean of float record array, axis = 0 : ", out_arr2)


# applying recarray.mean methods
# to float record array along axis 1
# i, e along horizontal
out_arr3 = rec_arr.a.mean(axis = 1)
# Mean along 0 axis
print("\nMean of float record array, axis = 1 : ", out_arr3)


# applying recarray.mean methods
# to int record array along default axis
# i, e along flattened array
out_arr4 = rec_arr.b.mean(dtype ='int')
# Mean of the flattened array
print("\nMean of int record array, axis = None : ", out_arr4)


# applying recarray.mean methods
# to int record array along axis 0
# i, e along vertical
out_arr5 = rec_arr.b.mean(axis = 0)
# Mean along 0 axis
print("\nMean of int record array, axis = 0 : ", out_arr5)


# applying recarray.mean methods
# to int record array along axis 1
# i, e along horizontal
out_arr6 = rec_arr.b.mean(axis = 1)
# Mean along 0 axis
print("\nMean of int record array, axis = 1 : ", out_arr6)
