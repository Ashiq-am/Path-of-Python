"""append() method only works for addition of elements at the end of the List,
for addition of element at the desired position, insert() method is used.
Unlike append() which takes only one argument, insert() method requires two arguments(position, value)."""


# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
