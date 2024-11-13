# IMPORT THE REQUIRED LIBRARY
import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://\
root:password@localhost/sakila")

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# GET THE `category` TABLE FROM THE METADATA OBJECT
category_table = meta_data.tables['category']

# SELECT category_id, name FROM category
# WHERE name IN ("Action", "Horror", "Sci-Fi");
query = db.select([
	category_table.c.category_id,
	category_table.c.name
]).where(
	category_table.c.name.in_([
		"Action", "Horror", "Sci-Fi"
	])
)

# FETCH ALL THE RECORDS IN THE RESPONSE
result = engine.execute(query).fetchall()

# VIEW THE ENTRIES IN THE RESULT
for record in result:
	print("\n", record)
