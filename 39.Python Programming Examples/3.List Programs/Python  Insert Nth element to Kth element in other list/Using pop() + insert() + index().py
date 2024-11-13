# Python3 code to demonstrate working of
# Insert Nth element to Kth element in other list
# Using pop() + index() + insert()

# initializing lists
test_list1 = [4, 5, 6, 7, 3, 8]
test_list2 = [7, 6, 3, 8, 10, 12]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing N
N = 5

# initializing K
K = 3

# Using pop() + index() + insert()
# Insert Nth element to Kth element in other list
res = test_list1.insert(K, test_list2.pop(N))

# Printing result
print("The list 1 after insert is : " + str(test_list1))
print("The list 2 after remove is : " + str(test_list2))
