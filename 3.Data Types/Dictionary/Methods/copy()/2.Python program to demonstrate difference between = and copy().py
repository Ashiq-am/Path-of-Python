# Python program to demonstrate difference
# between = and copy()
original = {1:'geeks', 2:'for'}

# copying using copy() function
new = original.copy()

# removing all elements from new list
# and printing both
new.clear()
print('new: ', new)
print('original: ', original)

original = {1:'one', 2:'two'}

# copying using =
new = original

# removing all elements from new list
# and printing both
new.clear()
print('new: ', new)
print('original: ', original)
