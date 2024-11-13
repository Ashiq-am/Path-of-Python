# Python code to demonstrate
# how to invert mapping
# using lambda

# initialising dictionary
ini_dict = {101 : "akshat", 201 : "ball"}

# print initial dictionary
print("initial dictionary : ", str(ini_dict))

# inverse mapping using lambda
lambda ini_dict: {v:k for k, v in ini_dict.items()}

# print final dictionary
print("inverse mapped dictionary : ", str(ini_dict))
