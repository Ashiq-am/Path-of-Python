import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://\
root:password@localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Students(Base):

	__tablename__ = 'students'

	first_name = db.Column(db.String(50),
						primary_key=True)
	last_name = db.Column(db.String(50),
						primary_key=True)
	course	 = db.Column(db.String(50))
	score	 = db.Column(db.Float)

# CREATE THE SESSION OBJECT
Session = sessionmaker(bind=engine)
session = Session()

# SELECTING COLUMN `first_name`, `last_name` WHERE `score > 80`
result = session.query(Students) \
	.with_entities(Students.first_name, Students.last_name) \
		.filter(Students.score > 80).all()

for r in result:
	print(r.first_name, r.last_name)
