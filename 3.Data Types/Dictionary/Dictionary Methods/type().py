''''''



"""Code #1"""


# Python3 simple code to explain
# the type() function
print(type([]) is list)

print(type([]) is not list)

print(type(()) is tuple)

print(type({}) is dict)

print(type({}) is not list)










"""Code #2"""


# Python3 code to explain
# the type() function

# Class of type dict
class DictType:
    DictNumber = {1: 'John', 2: 'Wick',
                  3: 'Barry', 4: 'Allen'}

    # Will print the object type
    # of existing class
    print(type(DictNumber))


# Class of type list
class ListType:
    ListNumber = [1, 2, 3, 4, 5]

    # Will print the object type
    # of existing class
    print(type(ListNumber))


# Class of type tuple
class TupleType:
    TupleNumber = ('Geeks', 'for', 'geeks')

    # Will print the object type
    # of existing class
    print(type(TupleNumber))


# Creating object of each class
d = DictType()
l = ListType()
t = TupleType()












"""Code #3"""


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













"""Code #4 : Use of type(name, bases, dict)"""

# Python3 program to demonstrate
# type(name, bases, dict)

# New class(has no base) class with the
# dynamic class initialization of type()
new = type('New', (object,),
           dict(var1='GeeksforGeeks', b=2009))

# Print type() which returns class 'type'
print(type(new))
print(vars(new))


# Base class, incorporated
# in our new class
class test:
    a = "Geeksforgeeks"
    b = 2009


# Dynamically initialize Newer class
# It will derive from the base class test
newer = type('Newer', (test,),
             dict(a='Geeks', b=2018))

print(type(newer))
print(vars(newer))
