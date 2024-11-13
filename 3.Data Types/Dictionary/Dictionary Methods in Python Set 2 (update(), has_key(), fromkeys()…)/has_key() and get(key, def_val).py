# Python code to demonstrate working of
# has_key() and get()

# Initializing dictionary
dict = { 'Name' : 'Nandini', 'Age' : 19 }

# using has_key() to check if dic1 has a key
if dict.has_key('Name'):
	print ("Name is a key")
else : print ("Name is not a key")

# using get() to print a key value
print ("The value associated with ID is : ")
print (dict.get('ID', "Not Present"))

# printing dictionary values
print ("The dictionary values are : ")
print (str(dict))
