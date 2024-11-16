# Python program explaining
# numpy.recarray.tobytes() method

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

# applying recarray.tobytes methods
# to float record array in default order
out_arr = rec_arr.a.tobytes()
print ("Output Python bytes of float record array in default order ", out_arr)
print()

# applying recarray.tobytes methods
# to float record array in fortan order
out_arr = rec_arr.a.tobytes(order ='F')
print ("Output Python bytes of float record array in fortan order ", out_arr)
print()

# applying recarray.tobytes methods
# to int record array in default order
out_arr = rec_arr.b.tobytes()
print ("Output Python bytes of int record array in default order ", out_arr)
print()

# applying recarray.tobytes methods
# to int record array in fortan order
out_arr = rec_arr.b.tobytes(order ='F')
print ("Output Python bytes of int record array in fortan order ", out_arr)
