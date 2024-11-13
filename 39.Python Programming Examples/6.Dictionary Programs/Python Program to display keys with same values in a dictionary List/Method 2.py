# initializing Matrix
test_list = [{"Gfg": 5, "is": 8, "best": 0},
			{"Gfg": 5, "is": 1, "best": 0},
			{"Gfg": 5, "is": 0, "best": 0}]

# printing original list
print("The original list is : " + str(test_list))

# getting keys
keys = list(test_list[0].keys())

res = []

# iterating each dictionary for similar key's value
for key in keys:

	# using all to check all keys with similar values
	flag = all(test_list[0][key] == ele[key] for ele in test_list)

	if flag:
		res.append(key)

# printing result
print("Similar values keys : " + str(res))
