# Python3 code to demonstrate working of
# Extract Dictionaries with given Key
# Using list comprehension + keys()

# initializing list
test_list = [{'gfg': 2, 'is': 8, 'good': 3},
			{'gfg': 1, 'for': 10, 'geeks': 9},
			{'love': 3}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
key = 'gfg'

# checking for key using in operator
# keys() used to get keys
res = [sub for sub in test_list if key in list(sub.keys())]

# printing result
print("The filtered Dictionaries : " + str(res))
