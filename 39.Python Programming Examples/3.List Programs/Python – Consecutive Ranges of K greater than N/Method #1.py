# Python3 code to demonstrate working of
# Consecutive Ranges of K greater than N
# Using loop

# initializing list
test_list = [2, 6, 6, 6, 6, 5, 4, 6,
			6, 8, 4, 6, 6, 6, 2, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

# initializing N
N = 3

res = []
strt, end = 0, 0
prev = 1
for idx, ele in enumerate(test_list):

	# if ele K assign end
	if ele == K:
		end = idx

		# if prev ele not K, reassign start
		if prev != K:	 # previous item one
			strt = idx
	else:

		# if range is greater than N, append to result
		if prev == K and end - strt + 1 >= N:
			res.append((strt, end))
	prev = ele

# printing result
print("The extracted ranges : " + str(res))
