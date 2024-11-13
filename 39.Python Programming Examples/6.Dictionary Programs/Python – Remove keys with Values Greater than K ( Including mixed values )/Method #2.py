# Python3 code to demonstrate working of
# Remove keys with Values Greater than K ( Including mixed values )
# Using dictionary comprehension + isinstance()

# initializing dictionary
test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 6

# using list comprehension to perform in one line
res = {key: val for key, val in test_dict.items() if not (isinstance(val, int) and (val > K))}

# printing result
print("The constructed dictionary : " + str(res))
