# Python program to demonstrate unzip (reverse
# of zip)using * with zip function

# Unzip lists
l1,l2 = zip(*[('Aston', 'GPS'),
			('Audi', 'Car Repair'),
			('McLaren', 'Dolby sound kit')
		])

# Printing unzipped lists
print(l1)
print(l2)
