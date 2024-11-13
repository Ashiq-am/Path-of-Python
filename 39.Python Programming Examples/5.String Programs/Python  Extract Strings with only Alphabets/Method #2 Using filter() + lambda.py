# Python3 code to demonstrate working of
# Extract Alphabet only Strings
# Using filter() + lambda

# initializing list
test_list = ['gfg', 'is23', 'best', 'for2', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Extract Alphabet only Strings
# Using filter() + lambda
res = list(filter(lambda sub: sub.isalpha(), test_list))

# printing result
print("Strings after filtering : " + str(res))
