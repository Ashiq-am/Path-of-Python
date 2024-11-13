# Python3 code to demonstrate working of
# Cross List Sync on duplicate elements removal
# Using loop + dict()

# initializing lists
test_list1 = [2, 2, 3, 4, 4, 4, 5, 5, 6, 6]
test_list2 = [8, 3, 7, 5, 4, 1, 0, 9, 4, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Cross List Sync on duplicate elements removal
temp = dict()
a = []
for idx in range(len(test_list1)):
    if test_list1[idx] not in a:
        a.append(test_list1[idx])

        # performing memoize using dictionary
        temp[test_list1[idx]] = test_list2[idx]

res2 = list(temp.values())
res1 = a

# printing result
print("List 1 : " + str(res1))
print("Sync List : " + str(res2))
