# Python 3 code to demonstrate
# behaviour with mutable objects

# initializing sequence and list
seq = { 'a', 'b', 'c', 'd', 'e' }
lis1 = [ 2, 3 ]

# using fromkeys() to convert sequence to dict
# using conventional method
res_dict = dict.fromkeys(seq, lis1)

# Printing created dict
print ("The newly created dict with list values : " + str(res_dict))

# appending to lis1
lis1.append(4)

# Printing dict after appending
# Notice that append takes place in all values
print ("The dict with list values after appending : " + str(res_dict))

lis1 = [ 2, 3 ]
print ('\n')

# using fromkeys() to convert sequence to dict
# using dict. comprehension
res_dict2 = { key : list(lis1) for key in seq }

# Printing created dict
print ("The newly created dict with list values : "
								+ str(res_dict2))

# appending to lis1
lis1.append(4)

# Printing dict after appending
# Notice that append doesnt take place now.
print ("The dict with list values after appending (no change) : "
											+ str(res_dict2))
