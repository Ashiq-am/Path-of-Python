from sqlalchemy import create_engine, Column, Integer, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.postgresql import JSONB, insert


engine = create_engine('postgresql://vikadmin:dbpass@localhost:5432/vikashdb')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Employee(Base):
	__tablename__ = 'employees'
	id = Column(Integer, primary_key=True)
	info = Column(JSONB)


employee_info = {
	'name': 'Vik Singh',
	'age': 35,
	'job_title': 'ML Engineer'
}

employee = Employee(id=15, info=employee_info)
session.add(employee)
session.commit()
