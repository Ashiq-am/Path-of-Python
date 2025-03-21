from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Database setup
engine = create_engine('sqlite:///:memory:')  # In-memory database for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
