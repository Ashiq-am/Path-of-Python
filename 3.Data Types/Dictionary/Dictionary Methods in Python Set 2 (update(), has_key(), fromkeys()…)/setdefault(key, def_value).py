# Python code to demonstrate working of
# setdefault()

# Initializing dictionary
dict = { 'Name' : 'Nandini', 'Age' : 19 }

# using setdefault() to print a key value
print ("The value associated with Age is : ",end="")
print (dict.setdefault('ID', "No ID"))

# printing dictionary values
print ("The dictionary values are : ")
print (str(dict))
