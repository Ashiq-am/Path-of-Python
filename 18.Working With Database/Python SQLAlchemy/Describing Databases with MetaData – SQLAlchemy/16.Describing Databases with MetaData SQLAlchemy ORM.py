from sqlalchemy.orm import relationship


class Student(Base):
	__tablename__ = 'student_account'
	id = Column(Integer, primary_key=True)
	name = Column(String(30))
	age = Column(Integer)
	grade = Column(String)

	addresses = relationship("Address", back_populates="student")

	def __repr__(self):
		return f"Student(id={self.id!r}, name={self.name!r},\
		age={self.age!r},grade={self.grade!r})"


class Address(Base):
	__tablename__ = 'address'
	id = Column(Integer, primary_key=True)
	email_address = Column(String, nullable=False)
	student_id = Column(Integer, ForeignKey('student_account.id'))

	student = relationship("Student", back_populates="addresses")

	def __repr__(self):
		return f"Address(id={self.id!r}, email_address={self.email_address!r})"
