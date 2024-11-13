''''''


'''Let’s say we want to count each element in a list and store in another list or say dictionary.'''



# Python3 program to count the number of times
# an object appears in a list using count() method

lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

# To get the number of occurrences
# of each item in a list
print ([ [l, lst.count(l)] for l in set(lst)])

# To get the number of occurrences
# of each item in a dictionary
print (dict( (l, lst.count(l) ) for l in set(lst)))
