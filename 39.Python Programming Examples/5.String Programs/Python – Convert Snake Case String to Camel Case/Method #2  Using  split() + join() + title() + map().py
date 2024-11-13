# Python3 code to demonstrate working of
# Convert Snake Case String to Camel Case
# Using split() + join() + title() + map()

# initializing string
test_str = 'geeksforgeeks_is_best'

# printing original string
print("The original string is : " + str(test_str))

# saving first and rest using split()
init, *temp = test_str.split('_')

# using map() to get all words other than 1st
# and titlecasing them
res = ''.join([init.lower(), *map(str.title, temp)])

# printing result
print("The camel case string is : " + str(res))
