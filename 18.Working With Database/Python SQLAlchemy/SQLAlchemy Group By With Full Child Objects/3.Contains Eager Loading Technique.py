from sqlalchemy.orm import contains_eager

# query
Query = session.query(Department,
		func.sum(Employee.salary).label("salary"))\
	.join(Employee)\
	.group_by(Department.name)\
	.options(contains_eager(Department.employees))

# executing the Query with DB
result = Query.all()

print("contains_eager technique result")
print("Dep salarySum")
for dep, salary in result:
	print(dep.name, salary)
