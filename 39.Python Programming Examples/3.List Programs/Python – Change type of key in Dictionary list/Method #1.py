# Python3 code to demonstrate working of
# Change type of key in Dictionary list
# Using loop

# initializing list
test_list = [{'gfg' : 1, 'is' : '56', 'best' : (1, 2)},
			{'gfg' : 5, 'is' : '12', 'best' : (6, 2)},
			{'gfg' : 3, 'is' : '789', 'best' : (7, 2)}]

# printing original list
print("The original list is : " + str(test_list))

# initializing change key
chnge_key = 'is'

# Change type of key in Dictionary list
# Using loop
for sub in test_list:
		sub[chnge_key] = int(sub[chnge_key])

# printing result
print("The converted Dictionary list : " + str(test_list))
