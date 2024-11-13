from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import defaultload
from sqlalchemy.ext.declarative import declarative_base
# Create Base class
Base = declarative_base()
# Establish connection
engine = create_engine("postgresql://postgres:root@localhost/test")
# Model classes
class Department(Base):
	__tablename__ = "department"
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	employees = relationship('Employee',
				back_populates="department")
class Employee(Base):
	__tablename__ = "employee"
	emp_id = Column(Integer, primary_key=True)
	emp_name = Column(String(50))
	age = Column(Integer)
	salary = Column(DECIMAL)
	dep_id = Column(Integer, ForeignKey("department.id"))
	department = relationship(
		"Department", back_populates="employees",
						overlaps="employees")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# Query to calculate the max age of employees in each department
query = session.query(Department, func.max(Employee.age)) \
			.join(Employee) \
			.group_by(Department.id, Department.name) \
			.options(defaultload(Department.employees))
result = query.all()
print("Default Loading")
print("dep Age")
for dep, max_age in result:
	print(dep.name, max_age)
session.close()
