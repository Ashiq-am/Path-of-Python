# Python3 code to demonstrate list
# concatenation using list comprehension

# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

# using list comprehension to concat
res_list = [y for x in [test_list1, test_list2] for y in x]

# Printing concatenated list
print ("Concatenated list using list comprehension: "
									+ str(res_list))
