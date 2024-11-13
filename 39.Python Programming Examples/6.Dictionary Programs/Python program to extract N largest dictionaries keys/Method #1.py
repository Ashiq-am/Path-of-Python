# Python3 code to demonstrate working of
# Extract top N Dictionaries by Key
# Using sorted() + lambda + reverse

# initializing dictionary
test_dict = {6 : 2, 8: 9, 3: 9, 10: 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing N
N = 4

res = []

# 0 in lambda used for keys, list sliced till N for top N values
for key, val in sorted(test_dict.items(), key = lambda x: x[0], reverse = True)[:N]:
	res.append(key)

# printing result
print("Top N keys are: " + str(res))
