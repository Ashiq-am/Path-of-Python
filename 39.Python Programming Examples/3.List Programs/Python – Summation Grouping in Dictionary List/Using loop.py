# Python3 code to demonstrate working of
# Summation Grouping in Dictionary List
# Using loop

# initializing list
test_list = [{'Gfg' : 1, 'id' : 2, 'best' : 8, 'geeks' : 10},
			{'Gfg' : 4, 'id' : 4, 'best': 10, 'geeks' : 12},
			{'Gfg' : 4, 'id' : 8, 'best': 11, 'geeks' : 15}]

# printing original list
print("The original list is : " + str(test_list))

# initializing group key
grp_key = 'Gfg'

# initializing sum keys
sum_keys = ['best', 'geeks']

# Summation Grouping in Dictionary List
# Using loop
res = {}
for sub in test_list:
	ele = sub[grp_key]
	if ele not in res:
		res[ele] = {x: 0 for x in sum_keys}
	for y in sum_keys:
		res[ele][y] += int(sub[y])

# printing result
print("The grouped list : " + str(res))
