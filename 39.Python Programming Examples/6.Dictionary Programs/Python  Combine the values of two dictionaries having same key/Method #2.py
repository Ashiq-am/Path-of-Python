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
# using dict() and items()
final_dictionary = dict(ini_dictionary1.items() + ini_dictionary2.items() +
					[(k, ini_dictionary1[k] + ini_dictionary2[k])
					for k in set(ini_dictionary2)
					& set(ini_dictionary1)])

# printing final result
print ("final dictionary", str(final_dictionary))
