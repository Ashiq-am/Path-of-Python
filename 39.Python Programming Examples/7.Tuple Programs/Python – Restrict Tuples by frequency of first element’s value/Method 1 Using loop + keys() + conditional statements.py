# Python3 code to demonstrate working of
# Restrict Tuples by frequency of first element's value
# Using loop + keys() + conditional statements

# initializing list
test_list = [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5),
			(3, 4), (1, 4), (3, 4), (4, 7)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = []
mem = dict()
for sub in test_list:

	# check in memory
	if sub[0] not in mem.keys():
		mem[sub[0]] = 1
	else:
		mem[sub[0]] += 1

	# add if less than K frequency
	if mem[sub[0]] <= K:
		res.append(sub)

# printing result
print("Filtered tuples : " + str(res))
