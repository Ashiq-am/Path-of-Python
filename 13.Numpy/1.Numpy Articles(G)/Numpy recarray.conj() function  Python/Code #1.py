# Python program explaining
# numpy.recarray.conj() method

# importing numpy as geek
import numpy as geek

# creating input array
in_arr = geek.array([[(5.0 + 2j, 2 + 1j), (3.0, -4 + 6j),
					(6.0-5j, 9)], [(9.0, 1), (5.0 + 1j, 4-1j),
					(-12.0 + 6j, -7 + 3j)]],
					dtype =[('a', complex), ('b', complex)])

print ("Input array : ", in_arr)

# convert it to a record array, using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)

# 1st record array
print("1st Record array of complex : ", rec_arr.a)

# applying recarray.conj methods to 1st record array
out_arr = (rec_arr.a).conj()
print ("Output 1st conjugated array : ", out_arr)

# 2nd record array
rec_arr = rec_arr.b
print("2nd Record array of complex : ", rec_arr)

# applying recarray.conj methods to 2nd record array
out_arr = rec_arr.conj()
print ("Output 2nd conjugated array : ", out_arr)
