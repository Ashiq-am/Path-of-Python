# Python3 code to demonstrate
# Pairing and combining nested list to tuple list
# using zip() + list comprehension

# initializing lists
test_list1 = [[1, 4, 5], [8, 7], [2]]
test_list2 = [['g', 'f', 'g'], ['f', 'r'], ['u']]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using zip() + list comprehension
# Pairing and combining nested list to tuple list
res = [(u, v) for x, y in zip(test_list1, test_list2)
							for u, v in zip(x, y)]

# print result
print("The paired list of tuple is : " + str(res))
