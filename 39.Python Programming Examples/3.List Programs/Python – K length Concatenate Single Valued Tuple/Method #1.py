# Python3 code to demonstrate working of
# K length Concatenate Single Valued Tuple
# Using zip() + list comprehension

# initializing lists
test_list = [(3, ), (6, ), (8, ), (2, ), (9, ), (4, )]

# printing original list
print("The original list is : " + str(test_list))

# K length Concatenate Single Valued Tuple
# Using zip() + list comprehension
res = [a + b for a, b in zip(test_list[::2], test_list[1::2])]

# printing result
print("Concatenated tuples : " + str(res))
