from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# create Base class
Base = declarative_base()

# Establish connection
engine = create_engine("mysql+pymysql://userName:password@host/dbName")

# model class


class Department(Base):
	__tablename__ = "department"
	id = Column(Integer, primary_key=True)
	name = Column(String(50))

	# the argument should be Class name not table name
	employees = relationship('Employee')


class Employee(Base):
	__tablename__ = "employee"
	emp_id = Column(Integer, primary_key=True)
	emp_name = Column(String(50))
	age = Column(Integer)
	salary = Column(DECIMAL)

	# dep_id is just to define the foreign key
	dep_id = Column(Integer, ForeignKey("department.id"))
	department = relationship("Department")


# creating tables in DB,if tables alredy creatd no need of these statement
Base.metadata.create_all(engine)


# creating session
Session = sessionmaker(bind=engine)
session = Session()


# creating instances of department class
ece_dep = Department(id=1, name="ECE")
cse_dep = Department(id=2, name="CSE")
mech_dep = Department(id=3, name="MECH")

# ece employees
emp1 = Employee(emp_id=101, emp_name="Kohli", age=34,
				salary=75000, dep_id=ece_dep.id)
emp2 = Employee(emp_id=102, emp_name="Dhoni", age=45,
				salary=120000, dep_id=ece_dep.id)
emp3 = Employee(emp_id=103, emp_name="Sachine", age=39,
				salary=100000, dep_id=ece_dep.id)

# cse employess
emp4 = Employee(emp_id=201, emp_name="Alice", age=26,
				salary=40000, dep_id=cse_dep.id)
emp5 = Employee(emp_id=202, emp_name="Bob",	 age=56,
				salary=75000, dep_id=cse_dep.id)
emp6 = Employee(emp_id=203, emp_name="charlie", age=43,
				salary=50000, dep_id=cse_dep.id)


# mech employees
emp7 = Employee(emp_id=301, emp_name="Ronaldo", age=56,
				salary=40000, dep_id=mech_dep.id)
emp8 = Employee(emp_id=302, emp_name="Messi", age=54,
				salary=30000, dep_id=mech_dep.id)
emp9 = Employee(emp_id=303, emp_name="neymar", age=45,
				salary=25000, dep_id=mech_dep.id)

# adding instances to session
session.add_all([ece_dep, cse_dep, mech_dep, emp1, emp2,
				emp3, emp4, emp5, emp6, emp7, emp8, emp9])

# committing the changes
session.commit()

# closing the connection
session.close()
