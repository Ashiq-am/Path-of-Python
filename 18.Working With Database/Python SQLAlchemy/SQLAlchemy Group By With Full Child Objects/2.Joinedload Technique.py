from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.declarative import declarative_base

# create Base class
Base = declarative_base()

# Establish connection
engine = create_engine("mysql+pymysql://user:password@host/dbName")


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


# creating tables in DB,if tables alredy
# creatd no need of these statement
Base.metadata.create_all(engine)

# creating session
Session = sessionmaker(bind=engine)
session = Session()

# query
joinloadQuery = session.query(Department,
                              func.count(Employee.emp_id).label("count")) \
    .join(Department.employees) \
    .group_by(Department) \
    .options(joinedload(Department.employees))

# execuing query with DB and fetching results
result = joinloadQuery.all()

print("Joinload technique result")
print("Dep Count")
for dep, count in result:
    print(dep.name, count)

# closing the connection
session.close()
