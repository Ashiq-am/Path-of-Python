from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Students(Base):

	__tablename__ = 'students'

	first_name = db.Column(db.String(50), primary_key=True)
	last_name = db.Column(db.String(50), primary_key=True)
	course = db.Column(db.String(50))
	score = db.Column(db.Float)


# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# SELECT first_name, last_name, SUM(score)
# AS total FROM students GROUP BY first_name, last_name;
result = session.query(Students) \
	.with_entities(
		Students.first_name,
		Students.last_name,
		db.func.sum(Students.score).label('total')
).group_by(
		Students.first_name,
		Students.last_name
).all()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
	print(r.first_name, r.last_name, "| Score =", r[2])
