from sqlalchemy import func

# add total marks obtained by each student in each subject
students = session.query(Student,
						func.sum(Student.marks).label(
	'total_marks')).group_by(Student.id).all()
for student_data in students:
	student = student_data[0]
	total_marks = student_data[1]
	print(student.name, total_marks)
