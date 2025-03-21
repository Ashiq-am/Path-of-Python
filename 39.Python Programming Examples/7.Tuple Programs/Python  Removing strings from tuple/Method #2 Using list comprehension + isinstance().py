# Python3 code to demonstrate
# Remove string from tuples
# using list comprehension + isinstance()

# initializing list
test_list = [('Geeks', 1, 2), ('for', 4, 'Geeks'), (45, 'good')]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + isinstance()
# Remove string from tuples
res = [tuple(j for j in i if not isinstance(j, str))
								for i in test_list]

# print result
print("The list after string removal is : " + str(res))
