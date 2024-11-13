# Python3 code to demonstrate
# indexing of sublist
# using enumerate() + next()

# initializing test list
test_list = [[1, 'Geeks'], [2, 'For'], [3, 'Geeks']]

# printing original list
print("The original list : " + str(test_list))

# using enumerate() + next()
# indexing of sublist
res = next((i for i, (j, ele) in enumerate(test_list) if ele == 'For'), None)

# print result
print("Index of nested element is : " + str(res))
