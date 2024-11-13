# Python3 code to demonstrate working of
# Extract Alphabet only Strings
# Using isalpha() + list comprehension

# initializing list
test_list = ['gfg', 'is23', 'best', 'for2', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Extract Alphabet only Strings
# Using isalpha() + list comprehension
res = [sub for sub in test_list if sub.isalpha()]

# printing result
print("Strings after filtering : " + str(res))
