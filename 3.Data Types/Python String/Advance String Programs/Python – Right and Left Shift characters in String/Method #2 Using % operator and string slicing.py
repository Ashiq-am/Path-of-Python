# Python3 code to demonstrate working of
# Right and Left Shift characters in String
# Using % operator and string slicing

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + test_str)

# initializing right rot
r_rot = 7

# initializing left rot
l_rot = 3

# Right and Left Shift characters in String
# Using % operator and string slicing
temp = (r_rot - l_rot) % len(test_str)
res = test_str[temp : ] + test_str[ : temp]

# printing result
print("The string after rotation is : " + str(res))
