# Python3 code to demonstrate working of
# Similar index pairs in Tuple lists
# Using list comprehension + zip()

# initializing lists
test_list1 = [(5, 6), (1, 2), (8, 9), (10, 33)]
test_list2 = [(8, 7), (1, 3), (11, 23), (9, 4)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Similar index pairs in Tuple lists
# Using list comprehension + zip()
res = [list(zip(a, b)) for a, b in zip(test_list1, test_list2)]

# printing result
print("The paired tuples : " + str(res))
