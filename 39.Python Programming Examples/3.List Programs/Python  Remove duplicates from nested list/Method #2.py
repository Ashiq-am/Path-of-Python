# Python3 code to demonstrate
# removing duplicate sublist
# using set() + map() + sorted()

# initializing list
test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
						[1, 2, 3], [3, 4, 1]]

# printing original list
print("The original list : " + str(test_list))

# using set() + map() + sorted()
# removing duplicate sublist
res = list(set(map(lambda i: tuple(sorted(i)), test_list)))

# print result
print("The list after duplicate removal : " + str(res))
