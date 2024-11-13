# Python program to demonstrate the
# difference in memory consumption
# of list and array

# importing array module
import array as arr

# importing system module
import sys

# declaring a list of 1000 elements
List = range(1000)

# printing size of each element of the list
print("Size of each element of" \
      " list in bytes: ", sys.getsizeof(List))

# printing size of the whole list
print("Size of the whole list in" \
      " bytes: ", sys.getsizeof(List) * len(List))

# declaring an array of 1000 elements
Array = arr.array('i', [1] * 1000)

# printing size of each
# element of the Numpy array
print("Size of each element of " \
      "the array in bytes: ", Array.itemsize)

# printing size of the whole Numpy array
print("Size of the whole array" " in bytes: ", len(Array) * Array.itemsize)
