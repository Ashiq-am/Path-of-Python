# Python code to demonstrate
# how to remove numeric digits from string
# using translate
from string import digits

# initialising string
ini_string = "Geeks123for127geeks"

# printing initial ini_string
print("initial string : ", ini_string)

# using translate and digits
# to remove numeric digits from string
remove_digits = str.maketrans('', '', digits)
res = ini_string.translate(remove_digits)

# printing result
print("final string : ", res)
