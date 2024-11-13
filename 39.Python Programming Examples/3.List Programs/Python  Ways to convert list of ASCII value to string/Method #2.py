# Python code to demonstrate
# conversion of list of ascii values
# to string

# Initialising list
ini_list = [71, 101, 101, 107, 115, 102,
			111, 114, 71, 101, 101, 107, 115]

# Printing initial list
print ("Initial list", ini_list)

# Using map and join
res = ''.join(map(chr, ini_list))

# Print the resultant string
print ("Resultant string", str(res))
