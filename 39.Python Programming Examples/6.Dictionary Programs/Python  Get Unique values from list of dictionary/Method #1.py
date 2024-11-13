# Python3 code to demonstrate working of
# Get Unique values from list of dictionary
# Using set() + values() + dictionary comprehension

# Initialize list
test_list = [{'gfg': 1, 'is': 2}, {'best': 1, 'for': 3}, {'CS': 2}]

# printing original list
print("The original list : " + str(test_list))

# Using set() + values() + dictionary comprehension
# Get Unique values from list of dictionary
res = list(set(val for dic in test_list for val in dic.values()))

# printing result
print("The unique values in list are : " + str(res))
