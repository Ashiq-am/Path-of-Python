''''''


"""Example #1"""


# Python program to show working
# of items() method in Dictionary

# Dictionary with three items
Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }

print("Dictionary items:")

# Printing all the items of the Dictionary
print(Dictionary1.items())










"""Example #2: To show working of items() after modification of Dictionary."""


# Python program to show working
# of items() method in Dictionary

# Dictionary with three items
Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }

print("Original Dictionary items:")

items = Dictionary1.items()

# Printing all the items of the Dictionary
print(items)

# Delete an item from dictionary
del[Dictionary1['C']]
print('Updated Dictionary:')
print(items)
