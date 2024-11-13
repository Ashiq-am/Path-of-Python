# Python3 code to demonstrate
# how to remove 'n' characters from starting
# of a string

# Initialising string
ini_string1 = 'garg_akshat'

# Initialising number of characters to be removed
n = 5

# Printing initial string
print("Initial String", ini_string1)

# Removing n characters from string using
# replace() function
res = ini_string1.replace(ini_string1[:5], '', 1)

# Printing resultant string
print("Resultant String", res)
