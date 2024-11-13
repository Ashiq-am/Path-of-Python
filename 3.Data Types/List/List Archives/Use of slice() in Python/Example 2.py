l = [('Student A', 9876543210, 'Address of A', 99, 82, 97, 78, 69),
	('Student B', 9999999999, 'Address of B', 90, 83, 87, 72, 67),
	('Student C', 8888888888, 'Address of C', 88, 41, 56, 61, 93)]

# Naming slice
details = slice(0, 3)
marks = slice(3, 8)

# display (name, address, phone no., avg marks) for each student
for student in l:
	print(student[details], "MArks:", sum(student[marks])/5)

# display average total marks of the class
sum_of_marks = 0
for student in l:
	sum_of_marks += sum(student[marks])
print(sum_of_marks / 3)
