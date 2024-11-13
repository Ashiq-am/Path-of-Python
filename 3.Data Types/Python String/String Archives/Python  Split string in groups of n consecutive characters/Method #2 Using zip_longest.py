# Python code to split string of number
# and character into every 4th number

# Importing
from itertools import zip_longest

# Group function using zip_longest to split
def group(n, iterable, fillvalue=None):
	args = [iter(iterable)] * n
	return zip_longest(fillvalue=fillvalue, *args)

# String initialization
str = '123GeeksForGeeks4567'

# Split point
n=4

# list of separated string
out_string = [''.join(lis) for lis in group(n, str, '')]

# Output list initialization
out_no = []

# Converting list of string into list of integer
for a in out_string:
	out_no.append(a)

# Printing list
print(out_no)
