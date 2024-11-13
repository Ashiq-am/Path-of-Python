import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine("mysql+pymysql:/\
/root:password@localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Students(Base):

	__tablename__ = 'students'

	first_name = db.Column(db.String(50),
						primary_key=True)
	last_name = db.Column(db.String(50),
						primary_key=True)
	course	 = db.Column(db.String(50))
	score	 = db.Column(db.Float)

# SQLAlCHEMY CORE QUERY TO FETCH SPECIFIC COLUMNS
query = db.select([Students.first_name, Students.last_name])

# FETCH ALL THE RECORDS IN THE RESPONSE
result = engine.execute(query).fetchall()

# VIEW THE ENTRIES IN THE RESULT
for record in result:
	print(record[0], record[1])
