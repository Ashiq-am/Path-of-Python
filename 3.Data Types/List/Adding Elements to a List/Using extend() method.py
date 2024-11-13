"""Other than append() and insert() methods, there’s one more method for Addition of elements, extend(),
this method is used to add multiple elements at the same time at the end of the list.

Note – append() and extend() methods can only add elements at the end."""

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)
