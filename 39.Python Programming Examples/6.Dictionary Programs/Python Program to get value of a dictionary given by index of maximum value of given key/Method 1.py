# initializing dictionary
test_dict = {"gfg": [4], "is": [1, 4, 8], "best": [9, 10]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing max_search key
max_search = "best"

# initializing output key
opt_key = "gfg"

# handling case in which maximum index is not
# present in output key
if len(test_dict[opt_key]) <= test_dict[max_search].index(
max(test_dict[max_search])):
	res = "Result not possible"

# using max() to get of search key
else:
	res = max(test_dict[opt_key], key=lambda sub: test_dict[max_search]
			[test_dict[opt_key].index(sub)])

# printing result
print("The required output : " + str(res))
