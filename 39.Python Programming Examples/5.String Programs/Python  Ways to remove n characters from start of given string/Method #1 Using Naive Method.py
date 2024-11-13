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
# Naive method
res = ''
for i in range(0, len(ini_string1)):
    if i >= n:
        res = res + ini_string1[i]

    # Printing resultant string
print("Resultant String", res)
