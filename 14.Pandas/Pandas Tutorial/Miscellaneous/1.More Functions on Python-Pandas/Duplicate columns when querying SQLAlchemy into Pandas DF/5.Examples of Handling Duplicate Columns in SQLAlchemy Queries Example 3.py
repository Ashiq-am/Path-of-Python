from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import pandas as pd

# Step 1: Set up SQLAlchemy engine for an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite database

# Step 2: Define the base class for ORM
Base = declarative_base()

# Define the 'Employee' class (ORM for employees table)
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    projects = relationship('Project', backref='employee')  # Relationship to projects

# Define the 'Project' class (ORM for projects table)
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    project_name = Column(String)
    budget = Column(Integer)
    employee_id = Column(Integer, ForeignKey('employees.id'))

# Step 3: Create the tables in the database
Base.metadata.create_all(engine)

# Step 4: Insert sample data into the tables using ORM
Session = sessionmaker(bind=engine)
session = Session()

employee1 = Employee(name='Sophia', department='Engineering', projects=[Project(project_name='Project A', budget=100000)])
employee2 = Employee(name='Liam', department='Marketing', projects=[Project(project_name='Project B', budget=150000)])

session.add(employee1)
session.add(employee2)
session.commit()

# Step 5: Query using ORM and join the tables
query = session.query(Employee.id.label('employee_id'), Employee.name.label('employee_name'),
                      Employee.department.label('employee_department'),
                      Project.id.label('project_id'), Project.project_name, Project.budget.label('project_budget'))\
               .join(Project)

# Step 6: Load the query result into a Pandas DataFrame
df = pd.read_sql(query.statement, session.bind)

# Display the result
print("Query using ORM to avoid duplicate columns:")
print(df)