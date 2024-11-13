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
	flag = 1
	for ele in test_list:

		# checking for similar values
		if test_list[0][key] != ele[key]:
			flag = 0
			break

	if flag:
		res.append(key)

# printing result
print("Similar values keys : " + str(res))
