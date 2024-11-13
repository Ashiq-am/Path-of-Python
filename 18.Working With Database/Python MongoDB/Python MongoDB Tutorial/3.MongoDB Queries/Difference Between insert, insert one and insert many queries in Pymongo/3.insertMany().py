# importing Mongoclient from pymongo
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["GFG"]

# Created or Switched to collection
# names: GeeksForGeeks
collection = db["College"]

mylist = [
    {"_id": 6, "name": "Deepanshu", "Roll No": "1006", "Branch": "CSE"},
    {"_id": 7, "name": "Anshul", "Roll No": "1007", "Branch": "IT"}
]

# Inseting the entire list in the collection
collection.insert_many(mylist)
