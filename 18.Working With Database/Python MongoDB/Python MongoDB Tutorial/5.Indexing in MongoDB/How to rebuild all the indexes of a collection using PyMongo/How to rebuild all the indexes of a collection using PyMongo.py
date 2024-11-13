# Python Program for demonstrating the
# rebuilding of indexes in MongoDB


# Importing required modules
from pymongo import MongoClient

# Connecting to MongoDB server
# client = MongoClient('host_name',
# 'port_number')
client = MongoClient('localhost', 27017)

# Connecting to the database named
# GFG
mydatabase = client.GFG

# Accessing the collection named
# Student
mycollection = mydatabase.Student

# Now rebuilding all the indexes of
# the collection
mycollection.reindex()
