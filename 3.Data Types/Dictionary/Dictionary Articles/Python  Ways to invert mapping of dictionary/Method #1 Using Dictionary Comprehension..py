# Python code to demonstrate
# how to invert mapping
# using dict comprehension

# initialising dictionary
ini_dict = {101: "akshat", 201 : "ball"}

# print initial dictionary
print("initial dictionary : ", str(ini_dict))

# inverse mapping using dict comprehension
inv_dict = {v: k for k, v in ini_dict.items()}

# print final dictionary
print("inverse mapped dictionary : ", str(inv_dict))
