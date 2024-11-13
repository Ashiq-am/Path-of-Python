"""Elements can be added to the List by using built-in append() function.
Only one element at a time can be added to the list by using append() method,
for addition of multiple elements with the append() method, loops are used.

Tuples can also be added to the List with the use of append method because tuples are immutable.
Unlike Sets, Lists can also be added to the existing list with the use of append() method."""


# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
	List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
