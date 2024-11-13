import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

class Actor(Base):
	__table__ = db.Table("actor", Base.metadata, autoload_with=engine)

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# SELECT COUNT(*) FROM Table LIMIT 1;
result = session.query(Actor).first()

# DISPLAY FIRST NAME OF FIRST RECORD IN ACTOR TABLE
print("First Name (Record 1):", result.first_name)
