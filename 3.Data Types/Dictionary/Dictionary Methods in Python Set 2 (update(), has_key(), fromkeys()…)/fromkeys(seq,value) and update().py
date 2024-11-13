# Python code to demonstrate working of
# fromkeys() and update()

# Initializing dictionary 1
dic1 = { 'Name' : 'Nandini', 'Age' : 19 }

# Initializing dictionary 2
dic2 = { 'ID' : 2541997 }

# Initializing sequence
sequ = ('Name', 'Age', 'ID')

# using update to add dic2 values in dic 1
dic1.update(dic2)

# printing updated dictionary values
print ("The updated dictionary is : ")
print (str(dic1))

# using fromkeys() to transform sequence into dictionary
dict = dict.fromkeys(sequ,5)

# printing new dictionary values
print ("The new dictionary values are : ")
print (str(dict))
