# Python3 code to demonstrate working of
# Split Dictionary values on size limit
# Using dictionary comprehension + enumerate() + list slicing

# initializing dictionary
test_dict = {1: "Geeksforgeeks",
			2: "best for", 3:
			"all geeks"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing limit
limit = 4

# cutting chunks of K
chunks = (sub[idx: idx + limit] for sub in test_dict.values()
		for idx in range(0, len(sub), limit))

# re assigning dictionary with chunks
res = {key: val for key, val in enumerate(chunks, 1)}

# printing result
print("The extracted values : " + str(res))
