# Python program to understand use
# of frozenset function

# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
		"college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing keys details
print('The frozen set is:', key)
