# importing MongoClient from pymongo
from pymongo import MongoClient

# importing ObjectId from bson library
from bson.objectid import ObjectId

# Establishing connection with
# mongodb on localhost
client = MongoClient('127.0.0.1', 27017)

# Access database object
db = client['database']

# Access collection object
collection = db['collection']
