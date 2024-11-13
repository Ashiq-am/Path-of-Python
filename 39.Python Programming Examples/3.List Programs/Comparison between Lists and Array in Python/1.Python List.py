# Python program to demonstrate
# some operations on list

# Declaring a List of integers
IntList = [10, 20, 30]
print("List of numbers: ")

# Printing the list
print(IntList)

# Declaring a List of strings
StrList = ["Geeks", "For", "Geeks"]
print("List of Strings: ")

# Printing the list
print(StrList)

# Declaring a list of non-homogeneous elements
Non_homogeneous_list = [10, "Geeks", 20.890,\
						"for", 30, "geeks"]
print("List of non-homogeneous elements: ")

# Printing the list
print(Non_homogeneous_list)

# Printing size of a list
print("Size of the Non-homogeneous list: ",\
			len(Non_homogeneous_list))

# Declaring a list
NewList = ["Geeks", "for", "Geeks"]
print("Original List: ", NewList)

# Adding an item to the list

# Adding an item in the list
# using the append method
NewList.append("the")

# Printing the modified list
print("After adding an element the"\
					"list becomes: ")
print(NewList)

# Adding an item in the list using the insert
# method to add an element at a specific position
NewList.insert(3, "is")

# Printing the modified list
print("After adding an element at"\
		"index 3 the list becomes: ")
print(NewList)

# Adding multiple items to the list at the
# end using extend method
NewList.extend(["best", "CS", "website"])

# Printing the modified list
print("After adding 3 elements at the"\
			"end, the list becomes: ")
print(NewList)

# Removing an item from the list

# Removing an element by
# writing the element itself
NewList.remove("the")

# Printing the modified list
print("After removing an element"\
			"the list becomes: ")
print(NewList)

# Removing an element by
# specifying its position
NewList.pop(3)

# Printing the modified list
print("After removing an element "\
	"from index 3 the list becomes: ")
print(NewList)
