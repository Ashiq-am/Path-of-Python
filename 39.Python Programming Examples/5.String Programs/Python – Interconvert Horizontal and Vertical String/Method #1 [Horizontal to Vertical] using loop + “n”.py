# Python3 code to demonstrate working of
# Interconvert Horizontal and Vertical String
# using [Horizontal to Vertical] using loop + "\n"

# initializing string
test_str = 'geeksforgeeks'

# printing original String
print("The original string is : " + str(test_str))

# using loop to add "\n" after each character
res = ''
for ele in test_str:
    res += ele + "\n"

# printing result
print("The converted string : " + str(res))
