# Python3 code to demonstrate working of
# Alternate characters reverse in String
# Using list comprehension

# initializing string
test_str = 'geeks4rgeeks'

# printing original string
print("The original string is : " + str(test_str))

# using one-liner to solve the problem
res = "".join(["".join(reversed(test_str[::2]))[idx] + test_str[1::2][idx]
               for idx in range(len("".join(reversed(test_str[::2]))))])

# printing result
print("Is alternate reversed string : " + str(res))
