# Python code to demonstrate
# how to add only numbers present
# in a list of characters and numbers

# initialising lists
ini_list = [1, 2, 3, 4, 'a', 'b', 'x', 5, 'z']

# printing initial list
print ("initial list", str(ini_list))

# code to add numbers from list
res = sum([x for x in ini_list if isinstance(x, int)])

# printing result
print ("resultant sum", res)
