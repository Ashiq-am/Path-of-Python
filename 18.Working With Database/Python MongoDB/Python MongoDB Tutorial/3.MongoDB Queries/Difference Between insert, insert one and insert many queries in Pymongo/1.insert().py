# importing Mongoclient from pymongo
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["GFG"]

# Created or Switched to collection
# names: College
collection = db["College"]

mylist = [
    {"_id": 1, "name": "Vishwash", "Roll No": "1001", "Branch": "CSE"},
    {"_id": 2, "name": "Vishesh", "Roll No": "1002", "Branch": "IT"},
    {"_id": 3, "name": "Shivam", "Roll No": "1003", "Branch": "ME"},
    {"_id": 4, "name": "Yash", "Roll No": "1004", "Branch": "ECE"},
]

# Inseting the entire list in the collection
collection.insert(mylist)
