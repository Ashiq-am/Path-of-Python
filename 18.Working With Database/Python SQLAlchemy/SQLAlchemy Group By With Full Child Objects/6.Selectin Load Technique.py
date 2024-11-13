from sqlalchemy.orm import selectinload

query = session.query(Department, func.min(Employee.salary)) \
			.join(Employee) \
			.group_by(Department.name) \
			.options(selectinload(Department.employees))

result = query.all()

for dep,salary in result:
	print(dep.name,salary)

session.close()
