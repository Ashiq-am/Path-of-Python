# Python3 code to demonstrate working of
# Sort Records by Kth Index List
# Using sort() + lambda

# initializing list
test_list = [([4, 5, 7, 3], 'Gfg'), ([8, 6, 3, 1], 'is'),
								([2, 3, 5, 2], 'best')]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# Sort Records by Kth Index List
# Using sort() + lambda
test_list.sort(key = lambda sub: sub[0][K])

# printing result
print("The records after sorting : " + str(test_list))
