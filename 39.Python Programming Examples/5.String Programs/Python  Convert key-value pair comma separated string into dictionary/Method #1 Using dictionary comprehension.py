# Python3 code to demonstrate
# converting comma separated string
# into dictionary

# Initialising string
ini_string1 = 'name = akshat, course = btech, branch = computer'

# Printing initial string
print("Initial String", ini_string1)

# Converting string into dictionary
# using dict comprehension
res = dict(item.split("=") for item in ini_string1.split(", "))

# Printing resultant string
print("Resultant dictionary", str(res))

