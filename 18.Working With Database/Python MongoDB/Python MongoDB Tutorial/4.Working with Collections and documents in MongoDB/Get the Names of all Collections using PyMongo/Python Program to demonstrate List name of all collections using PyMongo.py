# Python Program to demonstrate
# List name of all collections using PyMongo



# Importing required libraries
from pymongo import MongoClient


# Connecting to MongoDB server
# client = MongoClient('host_name', 'port_number')
client = MongoClient("localhost", 27017)


# Connecting to the database named
# GeeksForGeeks
mydatabase = client.GeeksForGeeks


# Getting the names of all the collections
# in GeeksForGeeks Database.
collections = mydatabase.list_collection_names()


# Printing the name of the collections to the console.
print(collections)
