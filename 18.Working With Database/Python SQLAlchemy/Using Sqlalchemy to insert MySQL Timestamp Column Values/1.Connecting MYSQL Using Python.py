# Import necessary libraries
import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP

# Create engine and sessionmaker
engine = create_engine(
	'mysql+mysqlconnector://root:1234@localhost:3306/gfg',
										echo=False)

# session instance is used to communicate with the database
Session = sessionmaker(bind=engine)
session = Session()
