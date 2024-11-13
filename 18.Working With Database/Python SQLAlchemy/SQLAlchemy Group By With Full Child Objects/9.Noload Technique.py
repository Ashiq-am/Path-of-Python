from sqlalchemy.orm import noload

query = session.query(Department, func.max(Employee.salary).label("maxSalary")) \
			.join(Employee,Department.id==Employee.dep_id) \
			.group_by(Department.id, Department.name) \
			.options(noload(Department.employees))\
			.all()
print("noload technique result")
print("Dep maxSalary")
for dep ,salary in query:
	print(dep.name,salary)

# closing the connection
session.close()
