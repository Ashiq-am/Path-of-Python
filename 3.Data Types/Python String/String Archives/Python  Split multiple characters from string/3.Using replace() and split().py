# Python code to demonstrate
# to split strings

# Initial string
data = "Let's_try, this now"

# printing original string
print("The original string is : " + data)

# Using replace() and split()
# Splitting characters in String
res = data.replace('_', ' ').replace(', ', ' ').split()

# Printing result
print("The list after performing split functionality : " + str(res))
