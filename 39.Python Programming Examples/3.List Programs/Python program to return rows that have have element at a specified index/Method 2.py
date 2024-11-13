# initializing lists
test_list1 = [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 4, 4]]
test_list2 = [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 1

# zip() combines elements together
res = []
[res.extend([t1, t2])
for t1, t2 in zip(test_list1, test_list2) if t1[K] == t2[K]]

# printing result
print("K index matching rows : " + str(res))
