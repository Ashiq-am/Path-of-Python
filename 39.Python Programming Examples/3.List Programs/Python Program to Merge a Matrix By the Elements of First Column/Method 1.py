# initializing list
test_list = [[4, "geeks"], [3, "Gfg"], [4, "CS"],
			[4, "cs"], [3, "best"]]

# printing original list
print("The original list is : " + str(test_list))

res = {}
for key, val in test_list:

	# setdefault used to merge similar values
	res.setdefault(key, []).append(val)

# getting all values
res = [[key] + val for key, val in res.items()]

# printing result
print("Merged Matrix : " + str(res))
