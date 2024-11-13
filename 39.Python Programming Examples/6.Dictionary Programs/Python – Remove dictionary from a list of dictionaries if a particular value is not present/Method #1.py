# Python3 code to demonstrate working of
# Remove dictionary if K value not present
# Using loop + values()

# initializing lists
test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},
			{"Gfg" : 5, "is": 8, "best" : 1},
			{"Gfg" : 3, "is": 7, "best" : 6},
			{"Gfg" : 3, "is": 7, "best" : 5}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 7

res = []

# using loop to check for K element
for sub in test_list:
	if K not in list(sub.values()):
		res.append(sub)

# printing result
print("Filtered dictionaries : " + str(res))
