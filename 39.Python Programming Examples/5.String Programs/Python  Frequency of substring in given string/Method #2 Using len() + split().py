# Python3 code to demonstrate working of
# Frequency of substring in string
# Using split() + len()

# initializing string
test_str = "GeeksforGeeks is for Geeks"

# initializing substring
test_sub = "Geeks"

# printing original string
print("The original string is : " + test_str)

# printing substring
print("The original substring : " + test_sub)

# using split() + len()
# Frequency of substring in string
res = len(test_str.split(test_sub))-1

# printing result
print("The frequency of substring in string is " + str(res))
