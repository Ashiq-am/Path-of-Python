import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["database"]

# Collection Name
col = db["GeeksForGeeks"]

# Fields with values as 1 will
# only appear in the result
x = col.find({},{'_id': 0, 'appliance': 1,
				'rating': 1, 'company': 1})

for data in x:
	print(data)
