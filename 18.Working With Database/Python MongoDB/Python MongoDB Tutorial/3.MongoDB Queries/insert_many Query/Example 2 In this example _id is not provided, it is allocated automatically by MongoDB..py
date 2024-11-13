# importing Mongoclient from pymongo
from pymongo import MongoClient


myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["GFG"]

# Created or Switched to collection
# names: GeeksForGeeks
collection = db["Geeks"]

# Creating a list of records which we
# insert in the collection using the
# update_many() method.
mylist = [
{"Manufacturer":"Honda", "Model":"City", "Color":"Black"},
{"Manufacturer":"Tata", "Model":"Altroz", "Color":"Golden"},
{"Manufacturer":"Honda", "Model":"Civic", "Color":"Red"},
{"Manufacturer":"Hyundai", "Model":"i20", "Color":"white"},
{"Manufacturer":"Maruti", "Model":"Swift", "Color":"Blue"},
]
# In the above list we do not specify the _id, the MongoDB assigns
# a unique id to all the records in the collection by default.

# Inseting the entire list in the collection
collection.insert_many(mylist)
