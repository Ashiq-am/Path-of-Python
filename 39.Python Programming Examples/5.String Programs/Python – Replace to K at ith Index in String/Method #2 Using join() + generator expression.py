# Python3 code to demonstrate working of
# Replace to K at ith Index in String
# using join() + generator expression

# initializing strings
test_str = 'geeks5geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '4'

# initializing i
i = 5

# the replaced result
res = ''.join(test_str[idx] if idx != i else K for idx in range(len(test_str)))

# printing result
print("The constructed string : " + str(res))
