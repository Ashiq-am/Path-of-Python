# Python3 code to demonstrate working of
# Mapping Matrix with Dictionary
# Using list comprehension

# initializing list
test_list = [[4, 2, 1], [1, 2, 3], [4, 3, 1]]

# printing original list
print("The original list : " + str(test_list))

# initializing dictionary
sub_dict = {1 : "gfg", 2: "best", 3 : "CS", 4 : "Geeks"}

# Using list comprehension to perform required mapping
# in one line
res = [[sub_dict[val] for val in sub] for sub in test_list]

# printing result
print("Converted Mapped Matrix : " + str(res))
