a = {'name': 'Alice', 'age': 25}

# Removes 'age' key
del a['age']
print(a)

# Removes 'name' key and returns its value
a.pop('name')
print(a)