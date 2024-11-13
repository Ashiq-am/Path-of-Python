students = session.query(Student).filter(
	and_(Student.id >= 100, Student.id <= 200,
		Student.dob > '2000-01-01')).all()
for student in students:
	print(student.name, student.dob, student.marks)
