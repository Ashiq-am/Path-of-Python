# Python3 code to demonstrate list
# concatenation using * operator

# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

# using * operator to concat
res_list = [*test_list1, *test_list2]

# Printing concatenated list
print ("Concatenated list using * operator : "
							+ str(res_list))
