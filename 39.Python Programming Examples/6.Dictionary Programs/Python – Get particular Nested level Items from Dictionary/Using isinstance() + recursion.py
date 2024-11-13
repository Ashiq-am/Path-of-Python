# Python3 code to demonstrate working of
# Get particular Nested level Items from Dictionary
# Using isinstance() + recursion

# helper function


def get_items(test_dict, lvl):

	# querying for lowest level
	if lvl == 0:
		yield from ((key, val) for key, val in test_dict.items()
					if not isinstance(val, dict))
	else:

		# recur for inner dictionaries
		yield from ((key1, val1) for val in test_dict.values()
					if isinstance(val, dict) for key1, val1 in get_items(val, lvl - 1))


# initializing dictionary
test_dict = {"Gfg": { "n1": 3, "nd2": { "n2": 6 }},
			"is": { "ne1": 5, "ndi2": { "ne2": 8, "ne22": 10 } }}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 2

# calling function
res = get_items(test_dict, K)

# printing result
print("Required items : " + str(dict(res)))
