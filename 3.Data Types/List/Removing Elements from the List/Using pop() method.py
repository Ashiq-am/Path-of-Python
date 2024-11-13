"""Pop() function can also be used to remove and return an element from the set,
but by default it removes only the last element of the set, to remove element from a specific position of the List,
index of the element is passed as an argument to the pop() method."""



List = [1,2,3,4,5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
