# Python program to demonstrate
# find_one() method

# Importing Library
from pymongo import MongoClient


# Connecting to MongoDB server
# client = MongoClient('host_name','port_number')
client = MongoClient('localhost', 27017)


# Connecting to the database named
# GFG
mydatabase = client.GFG


# Accessing the collection named
# gfg_collection
mycollection = mydatabase.Student


# Searching through the database
# using find_one method.
result = mycollection.find_one({"Branch":"CSE"}, {'_id':0, 'name':1, 'Roll No':1})
print(result)
