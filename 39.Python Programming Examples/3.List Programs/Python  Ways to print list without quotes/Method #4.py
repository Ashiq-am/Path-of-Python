# Python code to demonstrate
# printing list in proper way

# Initialising list
ini_list = ['a', 'b', 'c', 'd']

# Printing initial list with str
print ("List with str", str(ini_list))

translation = {39: None}
# Printing list using translate Method
print ("Printing list without quotes",
		str(ini_list).translate(translation))
