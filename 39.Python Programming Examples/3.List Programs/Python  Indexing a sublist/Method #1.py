# Python3 code to demonstrate
# indexing of sublist
# using list comprehension + index()

# initializing test list
test_list = [[1, 'Geeks'], [2, 'For'], [3, 'Geeks']]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + index()
# indexing of sublist
res = [ele for i, ele in test_list].index('For')

# print result
print("Index of nested element is : " + str(res))
