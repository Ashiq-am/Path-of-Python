d = {'name': 'John', 'age': 25}

# Add multiple key-value pairs
d.update({'city': 'New York', 'job': 'Engineer'})

print(d)

# Alternatively, you can pass a list of tuples:
d.update([('country', 'USA'), ('hobbies', 'reading')])

print(d)
# Output: {'name': 'John', 'age': 25, 'city': 'New York', 'job': 'Engineer',
#           'country': 'USA', 'hobbies': 'reading'}