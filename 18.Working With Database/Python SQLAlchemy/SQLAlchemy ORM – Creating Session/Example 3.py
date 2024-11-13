import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

# DEFINE THE ENGINE FOR DATABASE 1
engine_1 = db.create_engine("mysql+pymysql://\
root:password@localhost/Geeks4Geeks")

# DEFINE THE ENGINE FOR DATABASE 2
engine_2 = db.create_engine("mysql+pymysql://\
root:password@localhost/Geeks4Geeks2")

# CREATING A CONFIGURED SESSION
# CLASS FOR DATABASE 1
Session_1 = sessionmaker(bind=engine_1)
session_1 = Session_1()

# CREATING A SESSION CLASS FOR DATABASE
# 2 AND CONFIGURING IT LATER
Session_2 = sessionmaker()
Session_2.configure(bind=engine_2)
session_2 = Session_2()
