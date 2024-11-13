# Python3 code to demonstrate
# Retain K match index values from other list
# using zip() + list comprehension

# Initializing lists
test_list1 = ['Gfg', 'is', 'best', 'for', 'Geeks', 'and', 'CS']
test_list2 = [4, 1, 4, 3, 4, 2, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Initializing K
K = 4

# Group elements from Dual List Matrix
# using zip() + list comprehension
res = [x for x, y in zip(test_list1, test_list2) if y == K]

# printing result
print("The filtered list : " + str(res))
