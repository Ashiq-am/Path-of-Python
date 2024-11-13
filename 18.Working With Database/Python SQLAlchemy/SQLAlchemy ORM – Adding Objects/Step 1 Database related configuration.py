from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Syntax of database url = "<database_vendor_name>:
# //<username>:<password>@ip-address/hostname/
# <database_name>"
DB_URL = "postgresql://anurag:anurag@localhost/gfg"

engine = create_engine(DB_URL)

local_session = sessionmaker(autoflush=False,
							autocommit=False, bind=engine)

# With this we get a session to do whatever
# we want to do
db = local_session()
