# Python3 program for demonstration
# of list index() method

# Random list having sublist and tuple also
list1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')]

# Will print the index of sublist [9, 8, 7]
print(list1.index([9, 8, 7]))

# Will print the index of tuple
# ('cat', 'bat') inside list
print(list1.index(('cat', 'bat')))
