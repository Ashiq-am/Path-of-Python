from sqlalchemy.orm import Load

# Query to calculate the average salary of employees in each department
query = session.query(Department.name, func.avg(Employee.salary)) \
			.join(Employee, Employee.dep_id == Department.id) \
			.group_by(Department.name) \
			.options(Load(Employee))\
			.all()
print("Load technique result")
print("Dep averageSalary")
for depName, salary in query:
	print(depName, salary)

# closing the connection
session.close()
