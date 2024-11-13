# Python3 code to demonstrate working of
# Longest Alphabetic order of Kth index
# Using loop with sliding window

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks", "and", "cs"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

res = []
curr = test_list[:1]
for idx in range(1, len(test_list)):

	# checking for greater element
	if test_list[idx][K] <= test_list[idx - 1][K]:

		# comparing current with maximum length
		if len(curr) > len(res):
			res = curr
		curr = [test_list[idx]]
	else:
		curr.append(test_list[idx])
if len(curr) > len(res):
	res = curr

# printing result
print("Longest increasing Alphabetic order : " + str(res))
