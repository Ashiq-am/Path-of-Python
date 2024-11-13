# Declaring a dictionary
d = {}

# This is the list which we are
# trying to use as a key to
# the dictionary
a =[1, 2, 3, 4, 5]

# converting the list a to a string
p = str(a)
d[p]= 1

# converting the list a to a tuple
q = tuple(a)
d[q]= 1

for key, value in d.items():
	print(key, ':', value)
