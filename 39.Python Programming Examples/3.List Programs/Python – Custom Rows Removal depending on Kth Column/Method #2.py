# Python3 code to demonstrate
# Custom Rows Removal depending on Kth Column
# using list comprehension

# Initializing lists
test_list1 = [[3, 4, 5], [2, 6, 8], [1, 10, 2], [5, 7, 9], [10, 1, 2]]
test_list2 = [12, 4, 6]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Initializing K
K = 1

# Custom Rows Removal depending on Kth Column
# using list comprehension
res = [ele for ele in test_list1 if ele[K] not in test_list2]

# printing result
print("The matrix after rows removal is : " + str(res))
