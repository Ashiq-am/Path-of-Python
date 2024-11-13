# Python code to demonstrate namedtuple() and
# _fields and _replace()

# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',['name','age','DOB'])

# Adding values
S = Student('Nandini','19','2541997')

# using _fields to display all the keynames of namedtuple()
print ("All the fields of students are : ")
print (S._fields)

# using _replace() to change the attribute values of namedtuple
print ("The modified namedtuple is : ")
print(S._replace(name = 'Manjeet'))
