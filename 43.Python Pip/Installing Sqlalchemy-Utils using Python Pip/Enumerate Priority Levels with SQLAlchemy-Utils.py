from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class Task(Base):
	__tablename__ = 'tasks'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	priority = Column(ChoiceType(choices={'low': 'Low', 'medium': 'Medium', 'high': 'High'}), nullable=False)

Base.metadata.create_all(engine)
