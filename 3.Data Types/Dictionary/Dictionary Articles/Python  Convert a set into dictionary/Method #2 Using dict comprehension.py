# Python code to demonstrate
# converting set into dictionary
# using dict comprehension


# initializing set
ini_set = {1, 2, 3, 4, 5}

# printing intialized set
print ("initial string", ini_set)
print (type(ini_set))

str = 'fg'
# Converting set to dict
res = {element:'Geek'+str for element in ini_set}

# printing final result and its type
print ("final list", res)
print (type(res))
