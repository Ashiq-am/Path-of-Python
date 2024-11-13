# Python code to demonstrate
# printing list in a proper way

# Initialising list
ini_list = ['a', 'b', 'c', 'd']

# Printing initial list with str
print ("List with str", str(ini_list))

# Printing list using map
print ("List in proper method", '[%s]' % ', '.join(map(str, ini_list)))
