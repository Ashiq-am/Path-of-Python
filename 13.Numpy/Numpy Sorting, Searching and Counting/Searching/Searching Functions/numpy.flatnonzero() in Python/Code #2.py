# Python program using the indices of the non-zero
# elements as an index array to extract these elements

out_arr = arr.ravel()[geek.flatnonzero(arr)]

print ("Output array of non-zero number: ", out_arr)
