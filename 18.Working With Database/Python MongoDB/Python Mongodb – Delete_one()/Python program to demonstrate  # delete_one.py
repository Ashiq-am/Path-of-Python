# Python program to demonstrate
# delete_one


import pymongo


# creating Mongoclient object to
# create database with the specified
# connection URL
students = pymongo.MongoClient('localhost', 27017)

# connecting to a database with
# name GFG
Db = students["GFG"]

# connecting to a collection with
# name Geeks
coll = Db["Geeks"]

# creating query object
myQuery ={'Class':'2'}
coll.delete_one(myQuery)

# print collection after deletion:
for x in coll.find():
	print(x)
