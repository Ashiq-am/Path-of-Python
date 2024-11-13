""""""


'''Code #1 : Demonstrating the working of fromkeys()'''



# Python 3 code to demonstrate
# working of fromkeys()

# initializing sequence
seq = { 'a', 'b', 'c', 'd', 'e' }

# using fromkeys() to convert sequence to dict
# initializing with None
res_dict = dict.fromkeys(seq)

# Printing created dict
print ("The newly created dict with None values : " + str(res_dict))


# using fromkeys() to convert sequence to dict
# initializing with 1
res_dict2 = dict.fromkeys(seq, 1)

# Printing created dict
print ("The newly created dict with 1 as value : " + str(res_dict2))








"""
Behaviour of fromdict() with Mutable objects as values:

fromdict() can also be supplied with mulatable object as default value. But in this case, a deep copy is made of 
dictionary, i.e if we append value in original list, the append takes place in all the values of keys.

Prevention : Certain dictionary comprehension techniques can be used to create a new list as key values, 
that does not point to original list as values of keys.

"""






'''Code #2 : Demonstrating the behaviour with mutable objects.'''



# Python 3 code to demonstrate
# behaviour with mutable objects

# initializing sequence and list
seq = { 'a', 'b', 'c', 'd', 'e' }
lis1 = [ 2, 3 ]

# using fromkeys() to convert sequence to dict
# using conventional method
res_dict = dict.fromkeys(seq, lis1)

# Printing created dict
print ("The newly created dict with list values :"+ str(res_dict))

# appending to lis1
lis1.append(4)

# Printing dict after appending
# Notice that append takes place in all values
print ("The dict with list values after appending :"+ str(res_dict))

lis1 = [ 2, 3 ]
print ('\n')

# using fromkeys() to convert sequence to dict
# using dict. comprehension
res_dict2 = { key : list(lis1) for key in seq }

# Printing created dict
print ("The newly created dict with list values : "+ str(res_dict2))

# appending to lis1
lis1.append(4)

# Printing dict after appending
# Notice that append doesnt take place now.
print ("The dict with list values after appending (no change) : "+ str(res_dict2))
