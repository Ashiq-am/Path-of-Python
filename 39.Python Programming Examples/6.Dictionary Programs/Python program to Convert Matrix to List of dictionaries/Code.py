# initializing list
test_list = [["Gfg", [1, 2, 3]],
			["is", [6, 5, 4]], ["best", [9, 10, 11]]]

# printing original list
print("The original list : " + str(test_list))

# using loop to bind Matrix elements to dictionary
res = []
for key, val in test_list:

	for idx, val in enumerate(val):

		# append values according to rows structure
		if len(res) - 1 < idx:
			res.append({key: val})

		else:
			res[idx].update({key: val})

# printing result
print("Converted dictionary : " + str(res))
