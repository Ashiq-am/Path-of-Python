# Python3 code to demonstrate working of
# Sort dictionary by max / min element in value list
# Using sorted() + max() + dictionary comprehension + reverse + lambda

# initializing dictionary
test_dict = {"Gfg" : [6, 4], "is" : [10, 3], "best" : [8, 4],
			"for" : [7, 13], "geeks" : [15, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# lambda function driving maximum operation on sorted()
# dictionary comprehension used to reconstruct dictionary
res = {key: test_dict[key] for key in sorted(test_dict, key = lambda ele: max(test_dict[ele]),
	reverse = True)}

# printing result
print("Reverse Sorted dictionary on basis of max values : " + str(res))
