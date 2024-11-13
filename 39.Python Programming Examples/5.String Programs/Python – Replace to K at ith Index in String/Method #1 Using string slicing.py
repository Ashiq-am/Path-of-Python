# Python3 code to demonstrate working of
# Replace to K at ith Index in String
# using string slicing

# initializing strings
test_str = 'geeks5geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '4'

# initializing i
i = 5

# the replaced result
res = test_str[: i] + K + test_str[i + 1:]

# printing result
print("The constructed string : " + str(res))
