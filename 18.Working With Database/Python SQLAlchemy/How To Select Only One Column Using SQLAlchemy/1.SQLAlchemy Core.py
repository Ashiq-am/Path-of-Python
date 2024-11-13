import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE METADATA OBJECT
metadata_obj = db.MetaData()

# DEFINE THE PROFILE TABLE WITH 3 COLUMNS
profile = db.Table(
	'profile',
	metadata_obj,
	db.Column('email', db.String(50), primary_key=True),
	db.Column('name', db.String(100)),
	db.Column('contact', db.Integer),
)

# CREATE THE PROFILE TABLE IN THE DATABASE
metadata_obj.create_all(engine)

# INSERT RECORDS IN THE PRFILE TABLE
stmt = profile.insert().values(("amitpathak@zmail.com",
								"Amit Pathak",
								879456123))
engine.execute(stmt)
stmt = profile.insert().values(("amitmishra@zmail.com",
								"Amit Mishra",
								456789123))
engine.execute(stmt)
stmt = profile.insert().values(("ravipandey@zmail.com",
								"Ravi Pandey",
								321456987))
engine.execute(stmt)

# SQLAlCHEMY CORE QUERY TO FETCH SINGLE COLUMN (EMAIL)
query = db.select([profile.c.email])

# FETCH ALL THE RECORDS IN THE RESPONSE
result = engine.execute(query).fetchall()

# VIEW THE ENTRIES IN THE RESULT
for record in result:
	print("\n", record)
