# Python code to demonstrate
# how to invert mapping
# using map and reversed

# initialising dictionary
ini_dict = {101: "akshat", 201 : "ball"}

# print initial dictionary
print("initial dictionary : ", str(ini_dict))

# inverse mapping using map and reversed
inv_dict = dict(map(reversed, ini_dict.items()))

# print final dictionary
print("inverse mapped dictionary : ", str(inv_dict))
