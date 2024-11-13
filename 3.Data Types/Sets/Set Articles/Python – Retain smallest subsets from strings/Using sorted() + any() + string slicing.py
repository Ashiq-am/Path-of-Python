# Python3 code to demonstrate working of
# Retain smallest subsets from string
# Using sorted() + any() + string slicing

# initializing strings set
test_set = {'cbabca', 'cba', 'bdb', 'bdbab', 'abcx'}

# printing original string
print("The original set is : " + str(test_set))

res = set()
for st_r in sorted(test_set, key=len):

	# getting smallest set and checking for already
	# present smaller set for subset
	if not any(st_r[idx: idx + y + 1] in res
			for idx in range(len(st_r))
			for y in range(len(st_r) - idx)):
		res.add(st_r)

# printing result
print("Required extracted strings : " + str(res))
