# Python3 code to demonstrate working of
# Rear word replace in String
# using rfind() + join()

# initializing string
test_str = "GFG is good"

# printing original string
print("The original string is : " + test_str)

# initializing replace string
rep_str = "best"

# Rear word replace in String
# using rfind() + join()
res = test_str[: test_str.rfind(' ')] + ' ' + rep_str

# printing result
print("The String after performing replace : " + res)
