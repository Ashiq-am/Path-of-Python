from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///gfg.db', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    fees = relationship("Fee")


class Fee(Base):
    __tablename__ = 'fees'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))


Base.metadata.create_all(engine)

# now let us insert some data into these tables and then query the data with the relationship

Session = sessionmaker(bind=engine)
session = Session()

s1 = Student(name='John Doe', age=20)
session.add(s1)

f1 = Fee(amount=100, student_id=s1.id)
f2 = Fee(amount=200, student_id=s1.id)
session.add_all([f1, f2])

session.commit()

student_fees = session.query(Student).filter_by(name='John Doe').one().fees

for fee in student_fees:
    print(fee.amount)
