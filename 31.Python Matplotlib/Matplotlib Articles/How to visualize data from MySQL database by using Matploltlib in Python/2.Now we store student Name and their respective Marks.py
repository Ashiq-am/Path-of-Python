Names = []
Marks = []

for i in mycursor:
	Names.append(i[0])
	Marks.append(i[1])

print("Name of Students = ", Names)
print("Marks of Students = ", Marks)
