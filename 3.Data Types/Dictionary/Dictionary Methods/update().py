''''''


"""Example #1: Update with another Dictionary."""



# Python program to show working
# of update() method in Dictionary

# Dictionary with three items
Dictionary1 = { 'A': 'Geeks', 'B': 'For', }
Dictionary2 = { 'B': 'Geeks' }

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)








"""Example #2: Update with an iterable."""




# Python program to show working
# of update() method in Dictionary

# Dictionary with single item
Dictionary1 = { 'A': 'Geeks'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the Dictionary with iterable
Dictionary1.update(B = 'For', C = 'Geeks')
print("Dictionary after updation:")
print(Dictionary1)
