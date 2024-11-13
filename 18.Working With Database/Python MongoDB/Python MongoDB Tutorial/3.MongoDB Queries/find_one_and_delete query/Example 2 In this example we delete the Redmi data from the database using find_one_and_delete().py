# importing Mongoclient from pymongo
from pymongo import MongoClient


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["mydatabase"]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["GeeksForGeeks"]

# Defining the filter that we want to use.
Filter ={'Manufacturer': 'Redmi'}

# Using find_one_and_delete() function.
print("The returned document is:")
print(Collection.find_one_and_delete(Filter))

# Printing the data in the collection
# after find_one_and_delete() operation.
print("\nThe data after find_one_and_delete() operation is:")

for data in Collection.find():
	print(data)
