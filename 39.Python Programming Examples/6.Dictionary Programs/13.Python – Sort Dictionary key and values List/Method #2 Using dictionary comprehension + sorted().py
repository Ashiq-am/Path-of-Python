# Python3 code to demonstrate working of
# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()

# initializing dictionary
test_dict = {'gfg': [7, 6, 3],
			'is': [2, 10, 3],
			'best': [19, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()
res = {key : sorted(test_dict[key]) for key in sorted(test_dict)}

# printing result
print("The sorted dictionary : " + str(res))
