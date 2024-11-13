# Python3 code to demonstrate working of
# Consecutive Ranges of K greater than N
# Using enumerate() + zip() + list slice + list comprehension

# initializing list
test_list = [2, 6, 6, 6, 6, 5, 4, 6,
			6, 8, 4, 6, 6, 6, 2, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

# initializing N
N = 3

# getting break pairs indices
brk_pairs = [idx for idx, (x, y) in enumerate(
	zip(test_list, test_list[1:]),
1) if (x == K) != (y == K)]

# The ranges are checked for size required
res = [(idx, ele - 1) for idx, ele in zip([K] + brk_pairs,
										brk_pairs + [len(test_list)])
	if ele - idx >= N and test_list[idx] == K]

# printing result
print("The extracted ranges : " + str(res))
