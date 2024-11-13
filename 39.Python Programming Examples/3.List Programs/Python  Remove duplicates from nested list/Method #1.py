# Python3 code to demonstrate
# removing duplicate sublist
# using set() + sorted()

# initializing list
test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
						[1, 2, 3], [3, 4, 1]]

# printing original list
print("The original list : " + str(test_list))

# using set() + sorted()
# removing duplicate sublist
res = list(set(tuple(sorted(sub)) for sub in test_list))

# print result
print("The list after duplicate removal : " + str(res))
