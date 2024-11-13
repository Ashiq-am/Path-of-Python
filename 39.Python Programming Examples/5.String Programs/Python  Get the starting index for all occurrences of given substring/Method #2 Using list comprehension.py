# Python3 code to demonstrate
# to find all occurrences of substring in
# a string

# Initialising string
ini_string = 'xbzefdgstbzefzexezef'

# Initialising sub-string
sub_string = 'zef'

# Printing initial string and sub-string
print ("initial_strings : ", ini_string, "\nsubstring : ", sub_string)

res = []
# Finding all occurrences of substring
# in a string using list comprehension
res = [i for i in range(len(ini_string))
	if ini_string.startswith(sub_string, i)]

# printing result(
print ("resultant positions", str(res))
