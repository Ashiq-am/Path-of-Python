''''''



'''Example #1'''



# Python program to show working
# of setdefault() method in Dictionary

# Dictionary with single item
Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# using setdefault() method
Third_value = Dictionary1.setdefault('C')
print("Dictionary:", Dictionary1)
print("Third_value:", Third_value)








""" Example #2: When key is not in the dictionary."""




# Python program to show working
# of setdefault() method in Dictionary

# Dictionary with single item
Dictionary1 = { 'A': 'Geeks', 'B': 'For'}

# using setdefault() method
# when key is not in the Dictionary
Third_value = Dictionary1.setdefault('C')
print("Dictionary:", Dictionary1)
print("Third_value:", Third_value)

# using setdefault() method
# when key is not in the Dictionary
# but default value is provided
Fourth_value = Dictionary1.setdefault('D', 'Geeks')
print("Dictionary:", Dictionary1)
print("Fourth_value:", Fourth_value)

