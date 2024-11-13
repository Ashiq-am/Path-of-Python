# Python3 code to demonstrate
# Maximize Column in Records List
# using zip() + map()

# initializing list
test_list = [[(1, 4), (2, 3), (5, 2)], [(3, 7), (1, 9), (10, 5)]]

# printing original list
print("The original list : " + str(test_list))

# using zip() + map()
# Maximize Column in Records List
res = [tuple(map(max, zip(*i))) for i in zip(*test_list)]

# print result
print("The maximization of columns of tuple list : " + str(res))
