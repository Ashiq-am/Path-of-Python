# Python code to demonstrate
# how to invert mapping
# using zip and dict functions

# initialising dictionary
ini_dict = {101: "akshat", 201 : "ball"}

# print initial dictionary
print("initial dictionary : ", str(ini_dict))

# inverse mapping using zip and dict functions
inv_dict = dict(zip(ini_dict.values(), ini_dict.keys()))

# print final dictionary
print("inverse mapped dictionary : ", str(inv_dict))
