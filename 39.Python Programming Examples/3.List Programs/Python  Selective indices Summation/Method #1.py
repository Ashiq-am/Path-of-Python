# Python3 code to demonstrate
# Selective indices Summation
# using list comprehension + sum()

# initializing lists
test_list = [9, 4, 5, 8, 10, 14]
index_list = [1, 3, 4]

# printing original lists
print("Original list : " + str(test_list))
print("Original index list : " + str(index_list))

# using list comprehension + sum() to
# Selective indices Summation
res_list = sum([test_list[i] for i in index_list])

# printing result
print("Resultant list : " + str(res_list))
