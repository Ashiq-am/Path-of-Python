# importing library
import numpy

# initilizing list
lst = [1, 7, 0, 6, 2, 5, 6]

# converting list to array
arr = numpy.asarray(lst)

# displaying list
print ("List:", lst)

# displaying array
print ("arr: ", arr)

# made another array out of arr using asarray function
arr1 = numpy.asarray(arr)

#displaying arr1 before the changes made
print("arr1: " , arr1)

#change made in arr1
arr1[3] = 23

#displaying arr1 , arr , list after the change has been made
print("lst: " , lst)
print("arr: " , arr)
print("arr1: " , arr1)
