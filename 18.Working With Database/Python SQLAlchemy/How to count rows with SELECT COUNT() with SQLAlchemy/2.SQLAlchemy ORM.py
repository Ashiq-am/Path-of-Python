import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Actor(Base):

	__tablename__ = 'actor'

	actor_id = db.Column(db.SmallInteger,
							primary_key=True,
							autoincrement=True)
	first_name = db.Column(db.String(45))
	last_name = db.Column(db.String(45))
	last_update = db.Column(db.DateTime)
	city	 = db.Column(db.String(20))

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# SELECT COUNT(*) FROM Actor
result = session.query(Actor).count()

print("Count:", result)
