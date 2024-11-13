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
	course = db.Column(db.String(50), primary_key=True)
	score = db.Column(db.Float)


# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# SELECT * FROM students ORDER BY score DESC, course;
result = session.query(Students) \
	.order_by(
		Students.score.desc(),
		Students.course
).all()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
	print(r.first_name, r.last_name, r.course, r.score)
