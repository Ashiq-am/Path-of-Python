# Python3 code to demonstrate working of
# Convert string list into multiple cases
# Using map() + lambda + inbuilt functions

# Initializing list
test_list = ['bLue', 'ReD', 'yeLLoW']

# printing original list
print("The original list is : " + str(test_list))

# Convert string list into multiple cases
# Using map() + lambda + inbuilt functions
res = list(map(lambda ele: (ele.upper(), ele.title(), ele.lower()), test_list))

# printing result
print("The list with multiple cases are : " + str(res))
