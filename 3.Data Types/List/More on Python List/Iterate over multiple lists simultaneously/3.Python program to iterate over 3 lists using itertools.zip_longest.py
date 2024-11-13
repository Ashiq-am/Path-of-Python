# Python program to iterate
# over 3 lists using itertools.zip_longest

import itertools

num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

# Specifying default value as -1
for (a, b, c) in itertools.zip_longest(num, color, value, fillvalue=-1):
	print (a, b, c)
