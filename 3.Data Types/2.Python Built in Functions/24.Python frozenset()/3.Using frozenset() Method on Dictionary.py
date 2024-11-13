# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
		"college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing dict keys as frozenset
print('The frozen set is:', key)
