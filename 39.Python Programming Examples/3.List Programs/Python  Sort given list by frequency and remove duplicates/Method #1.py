# Python3 code to demonstrate
# sorting and removal of duplicates
# Using sorted() + set() + count()

# initializing list
test_list = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]

# printing original list
print("The original list : " + str(test_list))

# using sorted() + set() + count()
# sorting and removal of duplicates
res = sorted(set(test_list), key = lambda ele: test_list.count(ele))

# print result
print("The list after sorting and removal : " + str(res))
