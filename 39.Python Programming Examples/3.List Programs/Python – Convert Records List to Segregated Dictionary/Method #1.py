# Python3 code to demonstrate working of
# Convert Records List to Segregated Dictionary
# Using loop

# initializing list
test_list = [(1, 2), (3, 4), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing index value
frst_idx = "Gfg"
scnd_idx = 'best'

# Convert Records List to Segregated Dictionary
# Using loop
res = dict()
for sub in test_list:
	res[sub[0]] = frst_idx
	res[sub[1]] = scnd_idx

# printing result
print("The constructed Dictionary list : " + str(res))
