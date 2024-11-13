# Python3 code to demonstrate working of
# Replace multiple characters at once
# Using nested replace()

# initializing string
test_str = "abbabba"

# printing original string
print("The original string is : " + str(test_str))

# Using nested replace()
# Replace multiple characters at once
res = test_str.replace('a', '%temp%').replace('b', 'a').replace('%temp%', 'b')

# printing result
print("The string after replacement of positions : " + res)
