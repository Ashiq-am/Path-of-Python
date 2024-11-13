# Python3 code to demonstrate working of
# Cross List Sync on duplicate elements removal
# Using loop + zip()

# initializing lists
test_list1 = [2, 2, 3, 4, 4, 4, 5, 5, 6, 6]
test_list2 = [8, 3, 7, 5, 4, 1, 0, 9, 4, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Cross List Sync on duplicate elements removal
res1 = []
res2 = []

# both lists are combined index wise using zip()
for a, b in zip(test_list1, test_list2):
    if a not in res1:
        res1.append(a)
        res2.append(b)

# printing result
print("List 1 : " + str(res1))
print("Sync List : " + str(res2))
