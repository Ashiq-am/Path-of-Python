# Python code to demonstrate combining
# two dictionaries having same key

# initialising dictionaries
ini_dictionary1 = {'nikhil': 1, 'akash' : 5,
			'manjeet' : 10, 'akshat' : 15}
ini_dictionary2 = {'akash' : 7, 'akshat' : 5,
									'm' : 15}

# printing initial dictionaries
print ("initial 1st dictionary", str(ini_dictionary1))
print ("initial 2nd dictionary", str(ini_dictionary2))

# combining dictionaries
# using dict comprehension and set
final_dictionary = {x: ini_dictionary1.get(x, 0) + ini_dictionary2.get(x, 0)
					for x in set(ini_dictionary1).union(ini_dictionary2)}

# printing final result
print ("final dictionary", str(final_dictionary))
