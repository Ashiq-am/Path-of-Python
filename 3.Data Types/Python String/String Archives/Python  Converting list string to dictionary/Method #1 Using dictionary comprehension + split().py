# Python3 code to demonstrate
# Converting list string to dictionary
# Using dictionary comprehsion + split()

# initializing string
test_string = '[Nikhil:1, Akshat:2, Akash:3]'

# printing original string
print("The original string : " + str(test_string))

# using dictionary comprehsion + split()
# Converting list string to dictionary
res = {sub.split(":")[0]: sub.split(":")[1] for sub in test_string[1:-1].split(", ")}

# print result
print("The dictionary after extraction is : " + str(res))
