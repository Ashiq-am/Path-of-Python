# importing Mongoclient from pymongo
from pymongo import MongoClient


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["GFG"]

# Created or Switched to collection
# names: GeeksForGeeks
collection = db["Student"]

# Creating Dictionary of records to be
# inserted
records = {
	"record1": { "_id": 6,
	"name": "Anshul",
	"Roll No": "1006",
	"Branch": "CSE"},

	"record2": { "_id": 7,
	"name": "Abhinav",
	"Roll No": "1007",
	"Branch": "ME"}
}


# Inserting the records in the collection
# by using collection.insert_one()
for record in records.values():
	collection.insert_one(record)
