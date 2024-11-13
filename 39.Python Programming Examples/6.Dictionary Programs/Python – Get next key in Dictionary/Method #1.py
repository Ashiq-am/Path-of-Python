# Python3 code to demonstrate working of
# Get next key in Dictionary
# Using index() + loop

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing key
test_key = 'is'

# Get next key in Dictionary
# Using index() + loop
temp = list(test_dict)
try:
	res = temp[temp.index(test_key) + 1]
except (ValueError, IndexError):
	res = None

# printing result
print("The next key is : " + str(res))
