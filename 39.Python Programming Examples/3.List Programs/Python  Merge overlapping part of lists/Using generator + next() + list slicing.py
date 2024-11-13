# Python3 code to demonstrate working of
# Merge overlapping parts of list
# using generator + next() + list slicing

# initialize lists
test_list1 = [4, 5, 7, 9, 10, 11]
test_list2 = [10, 11, 16, 17]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Merge overlapping parts of list
# using generator + next() + list slicing
temp = (i for i in range(len(test_list2), 0, -1) if test_list2[:i] == test_list1[-i:])
temp2 = next(temp, 0)
res = test_list1 + test_list2[temp2 : ]

# printing result
print("List after overlapping merge is : " + str(res))
