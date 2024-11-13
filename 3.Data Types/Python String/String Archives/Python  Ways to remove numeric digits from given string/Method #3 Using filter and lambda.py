# Python code to demonstrate
# how to remove numeric digits from string
# using filter and lambda

# initialising string
ini_string = "akshat123garg"

# printing initial ini_string
print("initial string : ", ini_string)

# using filter and lambda
# to remove numeric digits from string
res = "".join(filter(lambda x: not x.isdigit(), ini_string))

# res = ini_string
# printing result
print("final string : ", str(res))
