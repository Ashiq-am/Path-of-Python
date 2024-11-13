from sqlalchemy.orm import raiseload

# query to get the minimum age in each department
query = session.query(Department, func.min(Employee.age)) \
			.join(Employee) \
			.group_by(Department.name) \
			.options(raiseload(Department.employees))

result = query.all()

print("Raise Lad technique")
print("Name MinAge")
for dep, age in result:
	print(dep.name, age)

session.close()
