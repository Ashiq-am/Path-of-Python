# Python code to demonstrate
# checking of element existence
# using set() + in
# using sort() + bisect_left()
from bisect import bisect_left

# Initializing list
test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using set() + in) : ")

# Checking if 4 exists in list
# using set() + in
test_list_set = set(test_list_set)
if 4 in test_list_set :
	print ("Element Exists")

print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")

# Checking if 4 exists in list
# using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4):
	print ("Element Exists")
