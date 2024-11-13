# Python3 code to demonstrate working of
# Return lowercase characters in string
# Using list comprehension + islower()

# initializing string
test_str = "GeeksForGeeKs"

# printing original string
print("The original string is : " + str(test_str))

# Return lowercase characters in string
# Using list comprehension + islower()
res = [char for char in test_str if char.islower()]

# printing result
print("The lowercase characters in string are : " + str(res))
