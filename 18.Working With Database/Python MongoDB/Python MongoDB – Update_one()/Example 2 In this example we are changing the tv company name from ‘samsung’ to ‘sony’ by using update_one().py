# importing Mongoclient from pymongo
from pymongo import MongoClient


conn = MongoClient('localhost', 27017)

# database
db = conn.database

# Created or Switched to collection
# names: GeeksForGeeks
collection = db.GeeksForGeeks

# Updating the tv company name from
# 'samsung' to 'sony'.
filter = { 'appliance': 'tv' }

# Values to be updated.
newvalues = { "$set": { 'company': "sony" } }

# Using update_one() method for single updation.
collection.update_one(filter, newvalues)

# Printing the updated content of the database
cursor = collection.find()
for record in cursor:
	print(record)
