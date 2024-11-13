# declare a dictionary of tuple with student data
data = {('bhanu', 10): 'student1',
		('uma', 12): 'student4',
		('suma', 11): 'student3',
		('ravi', 11): 'student2',
		('gayatri', 9): 'student5'}

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
