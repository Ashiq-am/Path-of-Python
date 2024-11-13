# Python3 code to demonstrate working of
# First occurrence of one list in another
# Using next() + set()

# initializing lists
test_list1 = [1, 6, 3, 7, 8, 9, 2]
test_list2 = [4, 10, 8, 2, 0, 11]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# converting test list to sets
test_list2 = set(test_list2)

# stops when 1st match element is found
res = next((ele for ele in test_list1 if ele in test_list2), None)

# printing result
print("First element in list 1 from 2 : " + str(res))
