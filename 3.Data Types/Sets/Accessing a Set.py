"""Set items cannot be accessed by referring to an index, since sets are unordered the items
has no index.
But you can loop through the set items using a for loop,
or ask if a specified value is present in a set, by using the in keyword."""





# Python program to demonstrate
# Accessing of elements in a set

# Creating a set
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
	print(i, end=" ")

# Checking the element
# using in keyword
print("Geeks" in set1)
