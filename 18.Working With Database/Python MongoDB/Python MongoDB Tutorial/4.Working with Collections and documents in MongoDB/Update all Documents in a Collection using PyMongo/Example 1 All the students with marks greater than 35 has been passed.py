from pymongo import MongoClient


# Creating an instance of MongoClient
# on default localhost
client = MongoClient('mongodb://localhost:27017')

# Accessing desired database and collection
db = client.gfg
collection = db["classroom"]

# Update passed field to be true for all
# students with marks greater than 35
collection.update_many(
	{"marks": { "$gt": "35" } },
		{
			"$set": { "passed" : "True" }
		}
)
