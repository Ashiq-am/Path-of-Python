# Python3 code to demonstrate working of
# Assign keys with Maximum element index
# Using max() + index() + loop

# initializing dictionary
test_dict = {"gfg": [5, 3, 6, 3], "is": [1, 7, 5, 3], "best": [9, 1, 3, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = dict()
for key in test_dict:

	# using index() to get required value
	res[key] = test_dict[key].index(max(test_dict[key]))

# printing result
print("The maximum index assigned dictionary : " + str(res))
