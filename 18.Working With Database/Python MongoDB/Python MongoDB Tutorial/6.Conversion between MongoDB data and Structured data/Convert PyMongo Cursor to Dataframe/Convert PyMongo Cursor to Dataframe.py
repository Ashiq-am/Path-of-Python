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
# gfg_collection
mycollection = mydatabase.College

# Now creating a Cursor instance
# using find() function
cursor = mycollection.find()
print('Type of cursor:',type(cursor))

# Converting cursor to the list of
# dictionaries
list_cur = list(cursor)

# Converting to the DataFrame
df = DataFrame(list_cur)
print('Type of df:',type(df))

# Printing the df to console
print()
print(df.head())
