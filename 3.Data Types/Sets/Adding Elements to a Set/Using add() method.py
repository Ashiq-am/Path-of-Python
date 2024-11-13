"""Elements can be added to the Set by using built-in add() function.
Only one element at a time can be added to the set by using add() method,
loops are used to add multiple elements at a time with the use of add() method.

Note – Lists cannot be added to a set as elements because Lists are not hashable whereas Tuples can be
added because tuples are immutable and hence Hashable."""




# Python program to demonstrate
# Addition of elements in a Set

# Creating a Set
set1 = set()
print("Intial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
	set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)
