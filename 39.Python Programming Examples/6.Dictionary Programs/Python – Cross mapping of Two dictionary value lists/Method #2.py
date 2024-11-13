# Python3 code to demonstrate working of
# Cross mapping of Two dictionary value lists
# Using list comprehension + dictionary comprehension

# initializing dictionaries
test_dict1 = {"Gfg" : [4, 7], "Best" : [8, 6], "is" : [9, 3]}
test_dict2 = {6 : [15, 9], 8 : [6, 3], 7 : [9, 8], 9 : [10, 11]}

# printing original lists
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# using internal and external comprehension to
# solve problem
res = {key: [j for i in val if i in test_dict2 for j in test_dict2[i]]
	for key, val in test_dict1.items()}

# printing result
print("The constructed dictionary : " + str(res))
