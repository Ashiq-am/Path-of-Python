# importing Mongoclient from pymongo
from pymongo import MongoClient

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["mydatabase"]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["GeeksForGeeks"]

# Filtering the Quantities greater
# than 40 using query.
cursor = Collection.find({"Quantity": {"$gt": 40}})

# Printing the filterd data.
print("The data having Quantity greater than 40 is:")
for record in cursor:
    print(record)

# Filtering the Quantities less
# than 40 using query.
cursor = Collection.find({"Quantity": {"$lt": 40}})

# Printing the filterd data.
print("\nThe data having Quantity less than 40 is:")
for record in cursor:
    print(record)
