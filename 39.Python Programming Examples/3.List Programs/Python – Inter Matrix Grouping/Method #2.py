# Python3 code to demonstrate working of
# Inter Matrix Grouping
# Using dictionary comprehension + dict()

# initializing lists
test_list1 = [[5, 8], [2, 0], [8, 4], [9, 3]]
test_list2 = [[8, 1], [9, 7], [2, 10], [5, 6]]

# printing original list
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# mapping dictionaries together, converting each row to dictionary
res = {key: [dict(test_list1)[key], dict(test_list2)[key]] for key in dict(test_list1)}

# printing result
print("The Grouped Matrix : " + str(dict(res)))
