# Python3 code to demonstrate
# to get elements from indices
# using map() + __getitem__

# initializing lists
test_list = [9, 4, 5, 8, 10, 14]
index_list = [1, 3, 4]

# printing original lists
print("Original list : " + str(test_list))
print("Original index list : " + str(index_list))

# using map() + __getitem__ to
# elements from list
res_list = map(test_list.__getitem__, index_list)

# printing result
print("Resultant list : " + str(res_list))
