# declare a dictionary of tuple with student data
data = {'student1': ('bhanu', 10), 'student4': ('uma', 12),
		'student3': ('suma', 11), 'student2': ('ravi', 11),
		'student5': ('gayatri', 9)}

# sort student dictionary based on items
for i in sorted(data.items()):
	print(i, end=" ")
print()

# sort student dictionary based on values
for i in sorted(data.values()):
	print(i, end=" ")
print()

# sort student dictionary based on keys
for i in sorted(data.keys()):
	print(i, end=" ")
