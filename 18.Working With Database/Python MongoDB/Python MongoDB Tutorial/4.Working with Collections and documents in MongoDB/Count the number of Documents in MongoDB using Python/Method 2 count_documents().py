from pymongo import MongoClient


Client = MongoClient()
myclient = MongoClient('localhost', 27017)

my_database = myclient["GFG"]
my_collection = my_database["Student"]

# number of documents in the collection
total_count = my_collection.count_documents({})
print("Total number of documents : ", total_count)
