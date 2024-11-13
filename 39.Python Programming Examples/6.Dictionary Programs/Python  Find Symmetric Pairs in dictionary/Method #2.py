# Python3 code to demonstrate working of
# Find Symmetric Pairs in dictionary
# Using list comprehension

# Initializing dict
test_dict = {'a' : 1, 'b' : 2, 'c' : 3, 1 : 'a', 2 : 'b'}

# printing original dict
print("The original dict is : " + str(test_dict))

# Find Symmetric Pairs in dictionary
# Using list comprehension
temp = [(key, value) for key, value in test_dict.items()]
res = [(x, y) for (x, y) in temp if (y, x) in temp]

# printing result
print("The pairs of Symmetric values : " + str(res))
