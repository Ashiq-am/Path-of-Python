# Python3 code to demonstrate working of
# Remove dictionary if K value not present
# Using list comprehension

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

# using one-liner to extract dicts with NO K value
# using not in operator to check presence
res = [sub for sub in test_list if K not in list(sub.values())]

# printing result
print("Filtered dictionaries : " + str(res))
