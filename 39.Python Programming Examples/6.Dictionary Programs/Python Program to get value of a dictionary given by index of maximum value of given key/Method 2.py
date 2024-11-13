# initializing dictionary
test_dict = {"gfg": [4, 1, 6], "is": [1, 4, 8], "best": [9, 10, 1]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing max_search key
max_search = "best"

# initializing output key
opt_key = "gfg"

# handling case in which maximum index is not present
# in output key
if len(test_dict[opt_key]) <= test_dict[max_search].index(
max(test_dict[max_search])):
	res = "Result not possible"

# using max() to get of search key
# zip() used for combining lists
else:
	res = max(zip(test_dict[opt_key], test_dict[max_search]),
			key=lambda sub: sub[1])[0]

# printing result
print("The required output : " + str(res))
