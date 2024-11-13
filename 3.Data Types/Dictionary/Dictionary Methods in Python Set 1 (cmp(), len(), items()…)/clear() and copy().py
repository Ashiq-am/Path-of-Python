# Python code to demonstrate working of
# clear() and copy()

# Initializing dictionary
dic1 = { 'Name' : 'Nandini', 'Age' : 19 }

# Initializing dictionary
dic3 = {}

# using copy() to make shallow copy of dictionary
dic3 = dic1.copy()

# printing new dictionary
print ("The new copied dictionary is : ")
print (dic3.items())

# clearing the dictionary
dic1.clear()

# printing cleared dictionary
print ("The contents of deleted dictionary is : ",end="")
print (dic1.items())
