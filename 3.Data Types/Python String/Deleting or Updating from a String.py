"""In Python, Updation or deletion of characters from a String is not allowed.
This will cause an error because item assignment or item deletion from a String is not supported.
Although deletion of entire String is possible with the use of a built-in del keyword.

This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned.
Only new strings can be reassigned to the same name."""





"""Updation of a character:"""


# Python Program to Update
# character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character
# of the String
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ")
print(String1)







"""Updating Entire String:"""


# Python Program to Update
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)









"""Deletion of a character:"""

# Python Program to Delete
# characters from a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character
# of the String
del String1[2]
print("\nDeleting character at 2nd Index: ")
print(String1)







"""Deleting Entire String:"""

# Python Program to Delete
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String
# with the use of del
del String1
print("\nDeleting entire String: ")
print(String1)



'''Deletion of entire string is possible with the use of del keyword. Further, if we try to print the string, 
this will produce an error because String is deleted and is unavailable to be printed.'''
