# Python program to demonstrate working
# of dictionary copy
original = {1:'geeks', 2:'for'}

# copying using copy() function
new = original.copy()

# removing all elements from the list
# Only new list becomes empty as copy()
# does shallow copy.
new.clear()

print('new: ', new)
print('original: ', original)
