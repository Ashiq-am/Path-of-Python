''''''




'''Example #1'''



# Python program to show working
# of has_key() method in Dictionary

# Dictionary with three items
Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks' }

# Dictionary to be checked
print("Dictionary to be checked: ")
print(Dictionary1)

# Use of has_key() to check
# for presence of a key in Dictionary
print(Dictionary1.has_key('A'))
print(Dictionary1.has_key('For'))











'''Example #2'''



# Python program to show working
# of has_key() method in Dictionary

# Dictionary with three items
Dictionary2 = { 1: 'Welcome', 2: 'To', 3: 'Geeks' }

# Dictionary to be checked
print("Dictionary to be checked: ")
print(Dictionary2)

# Use of has_key() to check
# for presence of a key in Dictionary
print(Dictionary2.has_key(1))
print(Dictionary2.has_key('To'))














""" 
NOTE: dict.has_key() has removed from Python 3.x

In Python 3.x, in operator is used to check whether a specified key is present or not in a Dictionary."""





# Python Program to search a key in Dictionary
# Using in operator

dictionary= {1:"Geeks",2:"For",3:"Geeks"}

print("Dictionary: {}".format(dictionary))

# Return True if Present.
if 1 in dictionary:		 # or "dictionary.keys()"
	print(dictionary[1])
else:
	print("{} is Absent".format(1))


# Return False if not Present.
if 5 in dictionary.keys():
	print(dictionary[5])
else:
	print("{} is Absent".format(5))

