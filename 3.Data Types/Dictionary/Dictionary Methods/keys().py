''''''

'''Example #1'''

# Python program to show working
# of keys in Dictionary

# Dictionary with three keys
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# Printing keys of dictionary
print(Dictionary1.keys())

# Creating empty Dictionary
empty_Dict1 = {}

# Printing keys of Empty Dictionary
print(empty_Dict1.keys())










"""Example #2: To show how updation of dictionary works"""

# Python program to show updation
# of keys in Dictionary

# Dictionary with two keys
Dictionary1 = {'A': 'Geeks', 'B': 'For'}

# Printing keys of dictionary
print("Keys before Dictionary Updation:")
keys = Dictionary1.keys()
print(keys)

# adding an element to the dictionary
Dictionary1.update({'C': 'Geeks'})

print('\nAfter dictionary is updated:')
print(keys)











"""Practical Application : The keys() can be used to access the elements of dictionary as we can do for list, 
without use of keys(), no other mechanism provides means to access dictionary keys as list by index. 
This is demonstrated in the example below."""









'''Example #3 : Demonstrating practical application of keys()'''

# Python program to demonstrate
# working of keys()

# initializing dictionary
test_dict = {("geeks"): 7, "for": 1, ("geeks"): 2}

# accessing 2nd element using naive method
# using loop
j = 0
for i in test_dict:
    if (j == 1):
        print('2nd key using loop : ' + i)
    j = j + 1

# accessing 2nd element using keys()
print('2nd key using keys() : ' + test_dict.keys()[1])
