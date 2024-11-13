# Python3 code to demonstrate working of
# Contruct dictionary Key-Value pairs separated by delim
# Using split() + loop

# initializing strings
test_str = 'gfg$3, is$9, best$10'

# printing original string
print("The original string is : " + str(test_str))

# initializing delim
delim = "$"

# split by comma for getting differnt dict values
dicts = test_str.split(', ')

res = dict()
for sub in dicts:

	# 2nd split for forming Key-Values for dictionary
	res[sub.split(delim)[0]] = sub.split(delim)[1]

# printing result
print("The constructed dictionary : " + str(res))
