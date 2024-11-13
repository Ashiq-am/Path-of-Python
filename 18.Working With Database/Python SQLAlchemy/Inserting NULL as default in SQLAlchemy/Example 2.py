import sqlalchemy as db

# CREATE THE METADATA OBJECT
metadata_obj = db.MetaData()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE SALES TABLE MODEL TO USE IT FOR QUERYING
sales = db.Table(
	'sales',
	metadata_obj,
	db.Column('product', db.String(50),
			primary_key=True),
	db.Column('quantity', db.String(100)),
	db.Column('description', db.Integer,
			default=None),
)

# CREATE SALES TABLE IF
# IT DOES NOT EXIST ALREADY
metadata_obj.create_all(engine)

# INSERT NEW RECORD WITH A DESCRIPTION
with engine.connect() as conn:
	conn.execute(
		db.insert(sales).values(
			product='Televisions',
			quantity=25,
			description='This value is inserted\
			using SQLAlchemy Core!'
		)
	)

# INSERT NEW RECORD WITHOUT DESCRIPTION SO
# THAT IT TAKES DEFAULT NULL VALUE AS DEFINED
with engine.connect() as conn:
	conn.execute(
		db.insert(sales).values(
			product='Laptops',
			quantity=31
		)
	)
