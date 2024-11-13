# Python program to show updation
# of keys in Dictionary

# Dictionary with two keys
Dictionary1 = {'A': 'Geeks', 'B': 'For'}

# Printing keys of dictionary
print("Keys before Dictionary Updation:")
keys = Dictionary1.keys()
print(keys)

# adding an element to the dictionary
Dictionary1.update({'C':'Geeks'})

print('\nAfter dictionary is updated:')
print(keys)
