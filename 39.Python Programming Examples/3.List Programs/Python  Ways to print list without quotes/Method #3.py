# Python code to demonstrate
# printing list in proper way

# Initialising list
ini_list = ['a', 'b', 'c', 'd']

# Printing initial list with str
print ("List with str", str(ini_list))

# Printing list using .format()
print ("Printing list without quotes", ("[{0}]".format(
					', '.join(map(str, ini_list)))))
