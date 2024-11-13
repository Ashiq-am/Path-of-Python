# Python3 code to demonstrate working of
# Incremental Slice concatenation in String list
# Using loop + slicing

# initializing list
test_list = ['gfg', 'for', 'all', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

res = ''
for idx in range(len(test_list)):
    # Incremental slicing
    res += test_list[idx][:idx + 1]

# printing result
print("Incremental sliced concatenated string : " + str(res))
