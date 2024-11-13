# initializing list
test_list = [{'gfg': 1, 'is': 4, 'best': 6},
			{'gfg': 10, 'is': 3, 'best': 7},
			{'gfg': 9, 'is': 4, 'best': 2},
			{'gfg': 4, 'is': 1, 'best': 0},
			{'gfg': 6, 'is': 3, 'best': 8}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key-values
key, value = 'gfg', 'best'

res = dict()
for sub in test_list:

	# constructed values
	res[sub[key]] = sub[value]

# printing result
print("Dictionary values : " + str(res))
