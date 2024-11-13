#subquery
subQuery=session\
	.query(Department.id, func.count(Employee.emp_id)\
	.label('employee_count'))\
	.join(Employee)\
	.group_by(Department.id)\
	.subquery()

#main query
mainQuery=session.query(Department,subQuery.c.employee_count)\
		.join(subQuery,Department.id == subQuery.c.id).all()

print("Subquery Technique")
for dep in mainQuery:
	print(dep[0].name,dep[1])

session.close()
