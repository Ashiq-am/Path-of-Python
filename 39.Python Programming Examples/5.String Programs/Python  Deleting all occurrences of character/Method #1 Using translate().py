# Python code to demonstrate working of
# Deleting all occurrences of character
# Using translate()

# initializing string
test_str = "GeeksforGeeks"

# initializing removal character
rem_char = "e"

# printing original string
print("The original string is : " + str(test_str))

# Using translate()
# Deleting all occurrences of character
res = test_str.translate(None, rem_char)

# printing result
print("The string after character deletion : " + str(res))
