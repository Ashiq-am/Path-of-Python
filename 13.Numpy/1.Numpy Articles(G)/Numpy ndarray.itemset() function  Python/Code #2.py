# Python program explaining
# numpy.ndarray.itemset() function

# importing numpy as geek
import numpy as geek

geek.random.seed(345)
arr = geek.random.randint(9, size =(3, 3))
print("Input array : ", arr)

arr.itemset((2, 2), 9)

print ("Output array : ", arr)
