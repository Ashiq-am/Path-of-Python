"""In order to access the items of a dictionary refer to its key name.Key can be used inside square brackets."""




# Python program to demonstrate
# accessing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])






"""There is also a method called get() that will also help in acessing the element from a dictionary."""




# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))









"""Accessing element of a nested dictionary"""


"""In order to access the value of any key in nested dictionary, use indexing [] syntax."""


# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
		'Dict2': {'Name': 'For'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
