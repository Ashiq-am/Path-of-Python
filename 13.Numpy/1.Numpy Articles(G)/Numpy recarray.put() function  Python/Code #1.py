# Python program explaining
# numpy.recarray.put() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([(1.0, 2), (3.0, -4), (5.0, 6),
					(7.0, 8), (9.0, -4), (11.0, -2)],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.put methods
# to float record array in default mode
rec_arr.a.put( [0, 2], [-14, 15])
print ("Output float array in default mode : ", rec_arr.a)

# applying recarray.put methods
# to float record array in clip mode
rec_arr.a.put( 13, -4, mode ='clip')
print ("Output float array in clip mode : ", rec_arr.a)

# applying recarray.put methods
# to int record array
rec_arr.b.put([1, 2, 4], [10, 15, 20])
print ("Output int array in default mode : ", rec_arr.b)

# applying recarray.put methods
# to int record array in clip mode
rec_arr.b.put(8, 100, mode ='clip')
print ("Output int array in clip mode : ", rec_arr.b)
