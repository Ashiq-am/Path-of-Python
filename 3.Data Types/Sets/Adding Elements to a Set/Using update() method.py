"""For addition of two or more elements Update() method is used.
The update() method accepts lists, strings, tuples as well as other sets as its arguments.
In all of these cases, duplicate elements are avoided."""






# Python program to demonstrate
# Addition of elements in a Set

# Addition of elements to the Set
# using Update function
set1 = set([ 4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)
