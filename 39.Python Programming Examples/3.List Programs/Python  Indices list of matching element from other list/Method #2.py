# Python3 code to demonstrate working of
# Indices list of matching element from other list
# Using list comprehension + set() + enumerate()

# initializing lists
test_list1 = [5, 7, 8, 9, 10, 11]
test_list2 = [8, 10, 11]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Indices list of matching element from other list
# Using list comprehension + set() + enumerate()
temp = set(test_list2)
res = [i for i, val in enumerate(test_list1) if val in temp]

# printing result
print("The matching element Indices list : " + str(res))
