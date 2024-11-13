# initializing Matrix
test_list = ["geeks", "weak", "beak", "peek"]

# printing original list
print("The original list is : " + str(test_list))

# getting min length string
min_len = min(len(ele) for ele in test_list)

res = []
for idx in range(0, min_len):

	# using all() for condition injection
	if all(ele[idx] == test_list[0][idx] for ele in test_list):
		res.append(test_list[0][idx])

# printing result
print("Extracted similar characters : " + str(res))
