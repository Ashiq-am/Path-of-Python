import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# GET THE `actor` TABLE FROM THE METADATA OBJECT
actor_table = meta_data.tables['actor']

# SELECT COUNT(*) FROM Actor
result = db.select([db.func.count()]).select_from(actor_table).scalar()

print("Count:", result)
