# Python3 code to demonstrate
# modifying tuple elements
# using zip() + list comprehension

# initializing lists
test_list1 = [('Geeks', 1), ('for', 2), ('Geeks', 3)]
test_list2 = [4, 5, 6]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using zip() + list comprehension
# modifying tuple elements
res = [(i[0], j) for i, j in zip(test_list1, test_list2)]

# print result
print("The modified resultant list of tuple : " + str(res))
