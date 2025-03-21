# Python3 code to demonstrate working of
# Filter dictionaries by values in Kth Key in list
# Using loop + conditional statements

# initializing list
test_list = [{"Gfg": 3, "is": 5, "best": 10},
			{"Gfg": 5, "is": 1, "best": 1},
			{"Gfg": 8, "is": 3, "best": 9},
			{"Gfg": 9, "is": 9, "best": 8},
			{"Gfg": 4, "is": 10, "best": 7}]

# printing original list
print("The original list is : " + str(test_list))

# initializing search_list
search_list = [1, 9, 8, 4, 5]

# initializing K
K = "best"

res = []
for sub in test_list:

	# checking if Kth key's value present in search_list
	if sub[K] in search_list:
		res.append(sub)

# printing result
print("Filtered dictionaries : " + str(res))
