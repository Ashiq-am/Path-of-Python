# Python3 code to demonstrate
# list slicing from K to end
# using None

# initializing list
test_list = [5, 6, 2, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# index to begin slicing
K = 2

# using None
# to perform list slicing from K to end
res = test_list[K : None]

# printing result
print ("The sliced list is : " + str(res))
