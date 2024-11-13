# Importing json module
import json

# Creating a dictionary
di = {1:'Nike', 2:'Gucci', 3:'Balenciaga', 4:'Fossil', 5: 'Lacoste'}
print(type(di))
print(f"Dictionary: {di}")

# Converting the dictionary into a string by using json.dumps() function
stri = json.dumps(di)
print(type(stri))
print(f"String: {stri}")
