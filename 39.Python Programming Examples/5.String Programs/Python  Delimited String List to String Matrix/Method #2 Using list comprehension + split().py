# Python3 code to demonstrate working of
# Delimited String List to String Matrix
# Using list comprehension + split()

# initializing list
test_list = ['gfg:is:best', 'for:all', 'geeks:and:CS']

# printing original list
print("The original list is : " + str(test_list))

# Delimited String List to String Matrix
# Using list comprehension + split()
res = [sub.split(':') for sub in test_list]

# printing result
print("The list after conversion : " + str(res))
