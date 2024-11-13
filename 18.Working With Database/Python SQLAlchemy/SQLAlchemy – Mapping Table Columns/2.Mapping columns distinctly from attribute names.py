import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# MAPPING TABLE ACTOR
class Actor(Base):

	__tablename__ = 'actor'

	id	 = db.Column('actor_id', db.SmallInteger, autoincrement=True,
						primary_key=True)
	fname	 = db.Column('first_name', db.String(45), nullable=False)
	lname	 = db.Column('last_name', db.String(45), nullable=False)
	update_on = db.Column('last_update', db.TIMESTAMP, nullable=False)

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# SELECT * FROM sakila.actor LIMIT 1;
result = session.query(Actor).first()

# DISPLAY FIRST NAME OF FIRST RECORD IN ACTOR TABLE
print("First Name (Record 1):", result.fname)
