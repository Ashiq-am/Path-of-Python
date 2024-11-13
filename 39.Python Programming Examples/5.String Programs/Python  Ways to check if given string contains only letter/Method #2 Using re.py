# Python code to demonstrate
# to find whether string contains
# only letters
import re

# Initialising string
ini_str = "ababababa"

# Printing initial string
print ("Initial String", ini_str)

# Code to check whther string contains only number
pattern = re.compile("^[a-zA-Z]+$")
if pattern.match(ini_str):
	print ("Contains only letters")
else:
	print ("Doesn't contains only letters")
