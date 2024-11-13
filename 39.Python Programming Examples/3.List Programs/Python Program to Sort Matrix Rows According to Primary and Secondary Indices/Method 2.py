import operator

# initializing list
test_list = [[2, 5, 7, 4], [8, 1, 3, 10], [9, 1, 9, 4], [10, 1, 1, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initializing pri, sec
pri, sec = 3, 2

# inplace sorting using sort()
res = sorted(test_list, key=operator.itemgetter(pri, sec))

# printing result
print("Matrix after sorting : " + str(res))
