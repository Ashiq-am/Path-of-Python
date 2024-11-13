import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Profile(Base):

	__tablename__ = 'profile'

	email = db.Column(db.String(50), primary_key=True)
	name = db.Column(db.String(100))
	contact = db.Column(db.Integer)

# SQLAlCHEMY CORE QUERY TO FETCH SINGLE COLUMN (EMAIL)
query = db.select([Profile.name])

# FETCH ALL THE RECORDS IN THE RESPONSE
result = engine.execute(query).fetchall()

# VIEW THE ENTRIES IN THE RESULT
for record in result:
	print("\n", record)
