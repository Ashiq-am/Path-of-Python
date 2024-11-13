from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select, union, intersect, except_

# Create a new connection to the SQLite database
engine = create_engine('sqlite:///employees.db', echo=True)

Base = declarative_base()

class Employee(Base):
	__tablename__ = 'employees'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)
	department = Column(String)

Base.metadata.create_all(engine)

# INTERSECT example

# Generating the two SELECT queries
select_1 = select([Employee]).where(Employee.age > 25)
select_2 = select([Employee]).where(Employee.department == 'IT')

# Performing the INTERSECT operation
intersect_query = select_1.intersect(select_2)

# Executing the query
result = engine.execute(intersect_query).fetchall()

# Displaying the result
for employee in result:
	print(employee.name, employee.age, employee.department)
