"""In Python Dictionary, Addition of elements can be done in multiple ways.
One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = ‘Value’.

Updating an existing value in a Dictionary can be done by using the built-in update() method.
Nested key values can also be added to an existing Dictionary.

Note- While adding a value, if the key value already exists,
the value gets updated otherwise a new Key with the value is added to the Dictionary."""




# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
