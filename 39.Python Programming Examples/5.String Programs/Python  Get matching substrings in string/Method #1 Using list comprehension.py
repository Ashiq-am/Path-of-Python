# Python3 code to demonstrate working of
# Get matching substrings in string
# Using list comprehension

# initializing string
test_str = "GfG is good website"

# initializing potential substrings
test_list = ["GfG", "site", "CS", "Geeks", "Tutorial" ]

# printing original string
print("The original string is : " + test_str)

# printing potential strings list
print("The original list is : " + str(test_list))

# using list comprehension
# Get matching substrings in string
res = [sub for sub in test_list if sub in test_str]

# printing result
print("The list of found substrings : " + str(res))
