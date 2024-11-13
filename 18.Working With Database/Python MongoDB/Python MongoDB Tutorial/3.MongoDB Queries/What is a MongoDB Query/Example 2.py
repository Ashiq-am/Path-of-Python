# importing Mongoclient from pymongo
from pymongo import MongoClient


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["mydatabase"]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["GeeksForGeeks"]

# Filtering the (Quantities greater than
# 40 AND greater than 40) using AND query.
cursor = Collection.find({"$and":[{"Quantity":{"$gt":40}}, {"Quantity":{"$gt":50}}]})

# Printing the filterd data.
print("Quantities greater than 40 AND Quantities greater than 40 :")
for record in cursor:
	print(record)

# Filtering the (Quantities greater than
# 40 OR greater than 40) using OR query.
cursor = Collection.find({"$or":[{"Quantity":{"$gt":40}},
								{"Quantity":{"$gt":50}}]})

# Printing the filterd data.
print()
print("Quantities greater than 40 OR Quantities greater than 40 :")
for record in cursor:
	print(record)
