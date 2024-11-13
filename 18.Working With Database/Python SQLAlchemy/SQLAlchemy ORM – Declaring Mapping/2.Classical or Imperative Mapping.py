from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.orm import mapper

# CREATE THE METADATA OBJECT REQUIRED TO CREATE THE TABLE
metadata = db.MetaData()

# DEFINE THE ACTOR TABLE USING SQLALCHEMY CORE
actor = db.Table(
	'actor',
	metadata,
	db.Column('actor_id', db.SmallInteger,
			autoincrement=True, primary_key=True),
	db.Column('first_name', db.String(45), nullable=False),
	db.Column('last_name', db.String(45), nullable=False),
	db.Column('last_update', db.TIMESTAMP, nullable=False, server_default=db.text(
		'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
)

# MAPPING CLASS ACTOR USING CLASSICAL MAPPING


class Actor(object):

	def __init__(self, first_name, last_name) -> None:
		self.first_name = first_name
		self.last_name = last_name


mapper(Actor, actor)

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# SELECT COUNT(*) FROM Actor
result = session.query(Actor).count()

print("Count of Records in Actor Table:", result)
print("Type of Actor Class:", type(Actor))
