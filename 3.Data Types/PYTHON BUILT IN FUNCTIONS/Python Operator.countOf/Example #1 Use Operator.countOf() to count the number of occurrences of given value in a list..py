# Python program showing
# use of countOf() function
# in a list

from operator import *
arr = [ 1, 2, 3, 3, 3 ]
arr1 = [ 'a', 'b', 'c', 'b', 'd' ]

print("Number of occurrence of b in arr1 =", countOf(arr1, "b"))
print("Number of occurrence of e in arr1 =", countOf(arr1, "e"))
print("Number of occurrence of 3 in arr =", countOf(arr, 3))
