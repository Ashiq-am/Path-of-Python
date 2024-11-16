# Python program explaining
# numpy.recarray.flatten() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(5.0, 2), (3.0, -4), (6.0, 9)],
					[(9.0, 1), (5.0, 4), (-12.0, -7)]],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.flatten methods
# to float record in Fortan order
out_arr1 = rec_arr.a.flatten(order ='F')
print ("Output float flattened array in Fortan order: ", out_arr1)

# applying recarray.flatten methods
# to float record array in default order
out_arr2 = rec_arr.a.flatten()
print ("Output float flattenedarray in default order : ", out_arr2)

# applying recarray.flatten methods
# to int record in 'A' order
out_arr3 = rec_arr.b.flatten(order ='A')
print ("Output int flattened array in A order: ", out_arr3)

# applying recarray.flatten methods
# to float record array in 'K' order
out_arr4 = rec_arr.b.flatten(order ='K')
print ("Output intt flattened array in K order : ", out_arr4)
