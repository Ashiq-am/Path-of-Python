# Python3 code to demonstrate working of
# Remove duplicate elements index from other list
# Using list comprehension + enumerate()

# initializing lists
test_list1 = [3, 5, 6, 5, 3, 7, 8, 6]
test_list2 = [1, 7, 6, 3, 7, 9, 10, 11]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# getting duplicate elements list using list comprehension
temp = [idx for idx, val in enumerate(test_list1) if val in test_list1[:idx]]

# excluding duplicate indices from other list
res = [ele for idx, ele in enumerate(test_list2) if idx not in temp]

# printing result
print("The list after removing duplicate indices : " + str(res))
