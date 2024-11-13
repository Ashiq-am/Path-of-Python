# Python code to demonstrate
# to remove trailing None
# elements from lists


# initialising lists
ini_list = [1, 2, 3, 4, None, 76, None, None, None]

# printing initial dictionary
print ("initial dictionary", str(ini_list))

# code toremove trailing None values
# from lists
res = [x for n, x in enumerate(ini_list)
	if any(y is not None for y in ini_list[n:])]

# printing result
print ("resultant list", str(res))
