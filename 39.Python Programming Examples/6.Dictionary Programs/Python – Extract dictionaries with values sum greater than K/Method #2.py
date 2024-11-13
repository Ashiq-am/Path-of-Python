# Python3 code to demonstrate working of
# Extract dictionaries with values sum greater than K
# Using list comprehension + sum()

# initializing lists
test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},
			{"Gfg" : 5, "is": 8, "best" : 1},
			{"Gfg" : 3, "is": 7, "best" : 6},
			{"Gfg" : 3, "is": 7, "best" : 5}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 15

# using one-liner to extract all the dictionaries
res = [sub for sub in test_list if sum(list(sub.values())) > K]

# printing result
print("Dictionaries with summation greater than K : " + str(res))
