# Python code to demonstrate
# changing keys of dictionary
# using naive method

# inititialising dictionary
ini_dict = {'nikhil': 1, 'vashu' : 5,
			'manjeet' : 10, 'akshat' : 15}

# printing initial json
print ("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['akash'] = ini_dict['akshat']
del ini_dict['akshat']


# printing final result
print ("final dictionary", str(ini_dict))
