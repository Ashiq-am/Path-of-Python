# Python3 code to demonstrate working of
# Convert string list into multiple cases
# Using inbuilt functions + list comprehension

# Initializing list
test_list = ['bLue', 'ReD', 'yeLLoW']

# printing original list
print("The original list is : " + str(test_list))

# Convert string list into multiple cases
# Using inbuilt functions + list comprehension
res = [(ele.upper(), ele.title(), ele.lower()) for ele in test_list]

# printing result
print("The list with multiple cases are : " + str(res))
