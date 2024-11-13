# Python3 code to demonstrate working of
# Equal Keys List Summation
# Using items() + list comprehension + sum()

# initializing dictionaries
test_dict1 = {'Gfg' : [1, 2, 3], 'for' : [2, 4], 'CS' : [7, 8]}
test_dict2 = {'Gfg' : [10, 11], 'for' : [5], 'CS' : [0, 18]}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Using items() + list comprehension + sum()
# Equal Keys List Summation
res = {key: sum(value) + sum(test_dict2[key]) for key, value in test_dict1.items()}

# printing result
print("The summation of dictionary values is : " + str(res))
