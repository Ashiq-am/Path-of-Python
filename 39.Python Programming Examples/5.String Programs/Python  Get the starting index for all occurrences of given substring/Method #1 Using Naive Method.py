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
flag = 0
k = 0

# Finding all occurrences of substring
# in a string using Naive method
for i in range(0, len(ini_string)):
	k = i
	flag = 0
	for j in range(0, len(sub_string)):
		if ini_string[k] != sub_string[j]:
			flag = 1
		if flag:
			break
		k = k + 1
	if flag == 0:
		res.append(i)


# printing result(
print ("resultant positions", str(res))
