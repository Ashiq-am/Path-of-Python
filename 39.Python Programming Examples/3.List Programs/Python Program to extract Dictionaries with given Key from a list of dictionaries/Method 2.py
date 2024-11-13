# Python3 code to demonstrate working of
# Extract Dictionaries with given Key
# Using filter() + lambda

# initializing list
test_list = [{'gfg': 2, 'is': 8, 'good': 3},
			{'gfg': 1, 'for': 10, 'geeks': 9},
			{'love': 3, 'gfg': 4}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
key = 'good'

# checking for key using in operator
# keys() used to get keys
# filter() + lambda used to perform fileration
res = list(filter(lambda sub: key in list(sub.keys()), test_list))

# printing result
print("The filtered Dictionaries : " + str(res))
