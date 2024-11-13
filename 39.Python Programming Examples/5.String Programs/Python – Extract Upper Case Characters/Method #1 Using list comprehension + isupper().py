# Python3 code to demonstrate working of
# Extract Upper Case Characters
# Using list comprehension + isupper()

# initializing string
test_str = "GeeksForGeeKs"

# printing original string
print("The original string is : " + str(test_str))

# Extract Upper Case Characters
# Using list comprehension + isupper()
res = [char for char in test_str if char.isupper()]

# printing result
print("The uppercase characters in string are : " + str(res))
