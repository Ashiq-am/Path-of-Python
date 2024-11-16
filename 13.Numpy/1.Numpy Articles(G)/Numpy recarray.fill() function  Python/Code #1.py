# Python program explaining
# numpy.recarray.fill() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([(5.0, 2), (3.0, -4), (6.0, 9),],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.fill methods
# to float record array
rec_arr.a.fill(5)
print ("Output filled array : ", rec_arr.a)

# applying recarray.fill methods
# to int record array
rec_arr.b.fill(0)
print ("Output filled array : ", rec_arr.b)
