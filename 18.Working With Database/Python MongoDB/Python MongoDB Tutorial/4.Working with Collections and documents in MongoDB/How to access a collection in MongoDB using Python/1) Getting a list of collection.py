from pymongo import MongoClient


# create an client instance of the
# MongoDB class
mo_c = MongoClient()

# create an instance of 'some_database'
db = mo_c.GFG

# get a list of a MongoDB database's
# collections
collections = db.list_collection_names()
print ("collections:", collections, "\n")
