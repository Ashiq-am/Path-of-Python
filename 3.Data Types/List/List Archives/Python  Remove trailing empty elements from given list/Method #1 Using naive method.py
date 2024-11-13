# Python code to demonstrate
# to remove trailing None
# elements from lists

# initialising lists
ini_list = [1, 2, 3, 4, None, 76, None, None, None]

# printing initial dictionary
print("initial dictionary", str(ini_list))

# code toremove trailing None values
# from lists
while not ini_list[-1]:
    ini_list.pop()

# printing result
print("resultant list", str(ini_list))
