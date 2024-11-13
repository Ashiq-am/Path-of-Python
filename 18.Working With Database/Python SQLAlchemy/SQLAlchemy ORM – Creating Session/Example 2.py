import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql:/\
/root:password@localhost/Geeks4Geeks")

# CREATE THE SESSION OBJECT
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

# session is configured later
Session.configure(bind=engine)
session = Session()
