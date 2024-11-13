# Python program to iterate
# over 3 lists using itertools.zip_longest

import itertools

num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

# iterates over 3 lists and till all are exhausted
for (a, b, c) in itertools.zip_longest(num, color, value):
	print (a, b, c)
