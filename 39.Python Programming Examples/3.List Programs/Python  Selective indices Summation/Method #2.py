# Python3 code to demonstrate
# Selective indices Summation
# using map() + __getitem__ + sum()

# initializing lists
test_list = [9, 4, 5, 8, 10, 14]
index_list = [1, 3, 4]

# printing original lists
print("Original list : " + str(test_list))
print("Original index list : " + str(index_list))

# using map() + __getitem__ + sum() to
# Selective indices Summation
res_list = sum(list(map(test_list.__getitem__, index_list)))

# printing result
print("Resultant list : " + str(res_list))
