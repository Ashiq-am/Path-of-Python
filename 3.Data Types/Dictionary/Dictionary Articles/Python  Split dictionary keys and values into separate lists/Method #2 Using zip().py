# Python code to demonstrate
# to split dictionary
# into keys and values

# initialising _dictionary
ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}

# printing iniial_dictionary
print("intial_dictionary", str(ini_dict))

# split dictionary into keys and values
keys, values = zip(*ini_dict.items())

# printing keys and values separately
print ("keys : ", str(keys))
print ("values : ", str(values))
