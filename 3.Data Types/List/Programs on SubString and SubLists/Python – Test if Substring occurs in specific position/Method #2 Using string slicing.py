# Python3 code to demonstrate working of
# Test if Substring occurs in specific position
# Using string slicing

# initializing string
test_str = "Gfg is best"

# printing original string
print("The original string is : " + test_str)

# initializing range
i, j = 7, 11

# initializing substr
substr = "best"

# Test if Substring occurs in specific position
# Using string slicing
res = test_str[i: j] == substr

# printing result
print("Does string contain substring at required position ? : " + str(res))
