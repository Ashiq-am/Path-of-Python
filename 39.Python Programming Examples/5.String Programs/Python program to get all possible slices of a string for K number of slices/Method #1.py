# Python3 code to demonstrate working of
# All possible slices for K length
# Using list comprehension + string slicing + loop

# initializing string
test_str = "Gfg4all"

# printing original string
print("The original string is : " + str(test_str))

# initializing number of slices
K = 3

res = [[test_str]]
for idx in range(K - 1):

	# slicing initial strings with difference sizes.
	res = [[*strt, end[:y], end[y:]] for *strt, end in res
		for y in range(1, len(end) - K + idx + 2)]

# printing result
print("All possible slices for K strings : " + str(res))
