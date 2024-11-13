# Python3 code to demonstrate
# Add substring at specific index
# using list slicing

# initializing string
test_string = 'geeksgeeks'

# initializing add_string
add_string = "for"

# printing original string
print("The original string : " + test_string)

# printing add string
print("The add string : " + add_string)

# initializing N
N = 5

# using list slicing
# Add substring at specific index
res = test_string[: N] + add_string + test_string[N:]

# print result
print("The string after performing addition : " + str(res))
