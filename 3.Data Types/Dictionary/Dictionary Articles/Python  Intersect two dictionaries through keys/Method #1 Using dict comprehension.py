# Python code to demonstrate
# intersection of two dictionaries
# using dict comprehension

# inititialising dictionary
ini_dict1 = {'nikhil': 1, 'vashu' : 5,
			'manjeet' : 10, 'akshat' : 15}
ini_dict2 = {'akshat' :15, 'nikhil' : 1, 'me' : 56}

# printing initial json
print ("initial 1st dictionary", ini_dict1)
print ("initial 2nd dictionary", ini_dict2)

# intersecting two dictionaries
final_dict = {x:ini_dict1[x] for x in ini_dict1
							if x in ini_dict2}

# printing final result
print ("final dictionary", str(final_dict))
