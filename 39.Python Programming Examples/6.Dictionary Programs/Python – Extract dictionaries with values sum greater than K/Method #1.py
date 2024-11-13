# Python3 code to demonstrate working of
# Extract dictionaries with values sum greater than K
# Using

# initializing lists
test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},
			{"Gfg" : 5, "is": 8, "best" : 1},
			{"Gfg" : 3, "is": 7, "best" : 6},
			{"Gfg" : 3, "is": 7, "best" : 5}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 15

# using loop to extract all dictionaries
res = []
for sub in test_list:
	sum = 0
	for key in sub:
		sum += sub[key]
	if sum > K:
		res.append(sub)

# printing result
print("Dictionaries with summation greater than K : " + str(res))
