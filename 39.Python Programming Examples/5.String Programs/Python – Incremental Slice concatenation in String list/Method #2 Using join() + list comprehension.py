# Python3 code to demonstrate working of
# Incremental Slice concatenation in String list
# Using join() + list comprehension

# initializing list
test_list = ['gfg', 'for', 'all', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# join performs concatenation
res = ''.join([test_list[idx][:idx + 1] for idx in range(len(test_list))])

# printing result
print("Incremental sliced concatenated string : " + str(res))
