# Python3 code to demonstrate
# how to remove 'n' characters from starting
# of a string

# Initialising string
ini_string1 = 'gargakshat123'

# Initialising number of characters to be removed
n = 5

# Printing initial string
print("Initial String", ini_string1)

# Removing n characters from a string
# This argument count length from zero
# So length to be stripped is passed n-1
res = ini_string1[4:]

# Printing resultant string
print("Resultant String", res)

