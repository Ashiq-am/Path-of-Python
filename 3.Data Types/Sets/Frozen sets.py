"""Frozen sets in Python are immutable objects that only support methods and operators that produce a result
without affecting the frozen set or sets to which they are applied.
While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
If no parameters are passed, it returns an empty frozenset."""





# Python program to demonstrate
# working of a FrozenSet

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')

Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset())
