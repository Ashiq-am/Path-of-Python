# Python3 code to demonstrate working of
# Change Datatype of Tuple Values
# Using list comprehension

# initializing list
test_list = [(4, 5), (6, 7), (1, 4), (8, 10)]

# printing original list
print("The original list is : " + str(test_list))

# Change Datatype of Tuple Values
# Using list comprehension
# converting to string using str()
res = [(x, str(y)) for x, y in test_list]

# printing result
print("The converted records : " + str(res))
