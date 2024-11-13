# Python3 code to demonstrate working of
# Removing Initial word from string
# Using partition()

# initializing string
test_str = "GeeksforGeeks is best"

# printing original string
print("The original string is : " + test_str)

# Using partition()
# Removing Initial word from string
res = test_str.partition(' ')[2]

# printing result
print("The string after omitting first word is : " + str(res))
