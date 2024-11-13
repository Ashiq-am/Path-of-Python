# Python3 code to explain
# the type() function

# Class of type dict
class DictType:
    DictNumber = {1: 'John', 2: 'Wick', 3: 'Barry', 4: 'Allen'}


# Class of type list
class ListType:
    ListNumber = [1, 2, 3, 4, 5]


# Creating object of each class
d = DictType()
l = ListType()

# Will print accordingly whether both
# the objects are of same type or not
if type(d) is not type(l):
    print("Both class have different object type.")
else:
    print("Same Object type")
