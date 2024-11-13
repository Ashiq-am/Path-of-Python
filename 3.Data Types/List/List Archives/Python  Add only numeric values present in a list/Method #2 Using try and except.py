# Python code to demonstrate
# how to add only numbers present
# in a list of characters and numbers

# initialising lists
ini_list = [1, 2, 3, 4, 'a', 'b', 'x', 5, 'z']

# printing initial list
print ("initial list", str(ini_list))

# code to add numbers from list
res = 0
for item in ini_list:
	try:
		res+= int(item)
	except ValueError:
		pass

# printing result
print ("resultant sum", res)
