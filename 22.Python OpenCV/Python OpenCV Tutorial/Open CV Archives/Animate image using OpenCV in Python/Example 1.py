a = ['-', '-', '-', 1, '-', '-', '-']
n = len(a) # length of the array

for i in range(2*n):
	# i is the index of the list a
	# i%n will have a value in range(0,n)
	# using slicing we can make the digit 1
	# appear to move across the list
	# this is similar to a cylic list
	print(a[(i % n):]+a[:(i % n)])
