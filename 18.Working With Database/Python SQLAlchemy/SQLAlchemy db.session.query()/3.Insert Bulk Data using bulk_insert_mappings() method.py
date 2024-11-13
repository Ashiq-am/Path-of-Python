from sqlalchemy import and_
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date
Base = declarative_base()


class Student(Base):
	__tablename__ = 'students'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	dob = Column(Date)
	marks = Column(Integer)


Base.metadata.create_all(engine)
students_data = [
	{'id': 122, 'name': 'Jane Smith',
				'dob': date(2002, 2, 1), 'marks': 90},
	{'id': 19, 'name': 'Bob Johnson',
	'dob': date(2001, 3, 1), 'marks': 75},
	{'id': 168, 'name': 'Alice Davis',
				'dob': date(1999, 4, 1), 'marks': 80},
]

session.bulk_insert_mappings(Student, students_data)
session.commit()
