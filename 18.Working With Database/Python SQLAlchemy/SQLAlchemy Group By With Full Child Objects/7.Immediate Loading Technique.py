result = session.query(Department,
		func.avg(Employee.age).label("averageAge"))\
			.join(Employee)\
			.group_by(Department.name)\
			.options(immediateload(Department.employees))\
			.all()

print("contains_eager technique result")
print("Dep averageAge")
for dep ,age in result:
	print(dep.name,age)

# closing the connection
session.close()
