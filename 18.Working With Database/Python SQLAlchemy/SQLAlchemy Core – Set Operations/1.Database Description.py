# importing required modules
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base

# Create a new connection to the SQLite database
engine = create_engine('sqlite:///employees.db', echo=True)

Base = declarative_base()


# Defining the Employee table
class Employee(Base):
	__tablename__ = 'employees'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)
	department = Column(String)

# Create the Employee table
Base.metadata.create_all(engine)

# Insert data into the table
from sqlalchemy.orm import sessionmaker

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# inserting values into the Employee table
session.add(Employee(name='John Doe', age=30, department='IT'))
session.add(Employee(name='Jane Smith', age=25, department='HR'))
session.add(Employee(name='John Smith', age=26, department='BD'))
session.add(Employee(name='Jane Doe', age=41, department='IT'))


session.commit()
