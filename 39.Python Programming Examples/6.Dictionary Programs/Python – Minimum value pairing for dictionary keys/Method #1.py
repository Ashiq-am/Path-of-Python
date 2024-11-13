# Python3 code to demonstrate working of
# Minimum value pairing for dictionary keys
# Using dict() + sorted() + zip() + lambda

# initializing lists
test_list1 = [4, 7, 4, 8, 7, 9]
test_list2 = [5, 7, 2, 9, 3, 4]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using zip() to bing key and value lists
# reverse sorting the list before assigning values
# so as minimum values get to end, and hence avoided from
# pairing
res = dict(sorted(zip(test_list1, test_list2), key = lambda ele: -ele[1]))

# printing result
print("The minimum paired dictionary : " + str(res))
