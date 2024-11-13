from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# MAPPING CLASS ACTOR USING DECLARATIVE MAPPING


class Actor(Base):

	__table_args__ = {'schema': 'sakila'}
	__tablename__ = 'actor'

	actor_id = db.Column(db.SmallInteger, autoincrement=True, primary_key=True)
	first_name = db.Column(db.String(45), nullable=False)
	first_name = db.Column(db.String(45), nullable=False)
	last_update = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text(
		'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# SELECT COUNT(*) FROM Actor
result = session.query(Actor).count()

print("Count of Records in Actor Table:", result)
print("Type of Actor Class:", type(Actor))
