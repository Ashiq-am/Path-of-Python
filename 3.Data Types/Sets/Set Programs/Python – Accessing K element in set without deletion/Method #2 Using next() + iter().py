# Python3 code to demonstrate working of
# Accessing K element in set without deletion
# Using next() + iter()

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing K
K = 7

set_iter = iter(test_set)
for idx in range(len(test_set)):

	# incrementing position
	ele = next(set_iter)
	if ele == K:
		break

# printing result
print("Position of K in set : " + str(idx))
