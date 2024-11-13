# Python3 code to demonstrate working of
# Frequency of substring in string
# Using count()

# initializing string
test_str = "GeeksforGeeks is for Geeks"

# initializing substring
test_sub = "Geeks"

# printing original string
print("The original string is : " + test_str)

# printing substring
print("The original substring : " + test_sub)

# using count()
# Frequency of substring in string
res = test_str.count(test_sub)

# printing result
print("The frequency of substring in string is " + str(res))
