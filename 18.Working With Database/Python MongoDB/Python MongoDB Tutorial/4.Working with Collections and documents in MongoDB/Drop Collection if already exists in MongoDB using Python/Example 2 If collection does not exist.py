import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database name
db = client["mydatabase"]

# Collection name
col = db["gfg"]

# drop collection col1
if col.drop():
	print('Deleted')
else:
	print('Not Present')
