# importing Mongoclient from pymongo
from pymongo import MongoClient

try:
	conn = MongoClient() # Making coonection

except:
	print("Could not connect to MongoDB")

# database
db = conn.database

# Created or Switched to collection
# names: GeeksForGeeks
collection = db.GeeksForGeeks

# Creating Records:
record1 = { "appliance":"fan",
		"quantity":10,
		"rating":"3 stars",
		"company":"havells"}
record2 = { "appliance":"cooler",
		"quantity":15,
		"rating":"4 stars",
		"company":"symphony"}
record3 = { "appliance":"ac",
		"quantity":20,
		"rating":"5 stars",
		"company":"voltas"}
record4 = { "appliance":"tv",
		"quantity":12,
		"rating":"3 stars",
		"company":"samsung"}

# Inserting the Data
rec_id1 = collection.insert_one(record1)
rec_id2 = collection.insert_one(record2)
rec_id3 = collection.insert_one(record3)
rec_id4 = collection.insert_one(record4)

# Printing the data inserted
print("The data in the database is:")
cursor = collection.find()
for record in cursor:
	print(record)
