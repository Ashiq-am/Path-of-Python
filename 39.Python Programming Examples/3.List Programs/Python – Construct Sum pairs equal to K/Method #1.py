# Python3 code to demonstrate working of
# Construct Sum pairs equal to K
# Using list comprehension + sum()

# initializing list
test_list = [3, 4, 0, 5, 2]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

# Construct Sum pairs equal to K
# Using list comprehension + sum()
res = [(test_list[idx], test_list[j]) for idx in range(len(test_list))
							for j in range(idx + 1, len(test_list))
						if sum((test_list[idx], test_list[j])) == K]

# printing result
print("The paired tuples equal to K : " + str(res))
