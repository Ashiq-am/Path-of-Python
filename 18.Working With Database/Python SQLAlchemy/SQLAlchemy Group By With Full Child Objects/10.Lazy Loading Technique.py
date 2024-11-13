departments = session.query(Department).all()
for department in departments:
	# Accessing the employees attribute triggers lazy loading
	employee_count = len(department.employees)
	print(f"Department: {department.name}, Employee Count: {employee_count}")
session.close()
