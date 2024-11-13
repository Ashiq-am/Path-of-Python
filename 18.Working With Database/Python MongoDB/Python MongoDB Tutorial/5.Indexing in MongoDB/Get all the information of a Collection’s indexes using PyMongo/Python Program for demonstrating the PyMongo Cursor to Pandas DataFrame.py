# Python Program for demonstrating the
# PyMongo Cursor to Pandas DataFrame


# Importing required modules
from pymongo import MongoClient
from pandas import DataFrame

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

# Displaying the information of all the indexes
# using the function index_information()
ind_info = mycollection.index_information()
print(ind_info)
