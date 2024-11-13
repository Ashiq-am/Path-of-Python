# Python3 code to demonstrate
# Specific Range Addition in List
# using list comprehension

# Initializing list
test_list = [4, 5, 6, 8, 10, 11]

# printing original list
print("The original list is : " + str(test_list))

# Initializing range
i, j = 2, 5

# Specific Range Addition in List
# using list comprehension
test_list[i : j] = [ele + 3 for ele in test_list[i : j]]

# printing result
print ("List after range addition : " + str(test_list))
