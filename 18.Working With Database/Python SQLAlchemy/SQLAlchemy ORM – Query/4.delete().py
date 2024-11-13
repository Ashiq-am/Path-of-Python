import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Profile(Base):

	__tablename__ = 'profile'

	email = db.Column(db.String(50), primary_key=True)
	name = db.Column(db.String(100))
	contact = db.Column(db.Integer)

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# DELETE FROM profile WHERE email = 'ravipandey@zmail.com'
result = session.query(Profile) \
	.filter(Profile.email == 'ravipandey@zmail.com') \
		.delete(synchronize_session=False)
print("Rows deleted:", result)

result = session.query(Profile).count()
print("Total records:", result)
