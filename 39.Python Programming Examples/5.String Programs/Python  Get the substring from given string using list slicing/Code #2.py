# Python3 code to demonstrate
# to create a substring from string

# Initialising string
ini_string = 'xbzefdgstb'

# printing initial string and character
print ("initial_strings : ", ini_string)

# creating substring by taking element
# after certain position gap
# define length upto which substring required
sstring_alt = ini_string[::2]
sstring_gap2 = ini_string[::3]

# printing result
print ("print resultant substring from start", sstring_alt)
print ("print resultant substring from end", sstring_gap2)
