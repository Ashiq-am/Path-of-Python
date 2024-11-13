# Python3 code to demonstrate working of
# Remove odd elements from value lists in dictionary
# Using list comprehension + dictionary comprehension

# initializing Dictionary
test_dict = {'gfg' : [1, 3, 4, 10], 'is' : [1, 2, 8], 'best' : [4, 3, 7]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Remove odd elements from value lists in dictionary
# Using list comprehension + dictionary comprehension
res = {key: [idx for idx in val if idx % 2]
		for key, val in test_dict.items()}

# printing result
print("The filtered values are : " + str(res))
