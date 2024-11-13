# Python3 code to demonstrate
# list slicing from K to end
# without specifying last element

# initializing list
test_list = [5, 6, 2, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# index to begin slicing
K = 2

# without specifying last element
# to perform list slicing from K to end
res = test_list[K :]

# printing result
print ("The sliced list is : " + str(res))
