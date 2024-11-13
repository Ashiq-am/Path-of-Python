# Python program to demonstrate
# create_index() method


# Importing Library
from pymongo import MongoClient, ASCENDING


# Connecting to MongoDB server
# client = MongoClient('host_name', 'port_number')
client = MongoClient('localhost', 27017)


# Connecting to the database named
# GFG
mydatabase = client.GFG


# Accessing the collection named
# gfg_collection
mycollection = mydatabase.Student

mycollection.create_index('Roll No', unique = True)


# Inserting into Database
mycollection.insert_one({'_id':8 ,
						'name': 'Deepanshu',
						'Roll No': '1008',
						'Branch': 'IT'})

# Inserting with the same Roll no again.
# As the Roll no field is the index and
# is set to unique it will through the error.
mycollection.insert_one({'_id':9 ,
						'name': 'Hitesh',
						'Roll No': '1008',
						'Branch': 'CSE'})
