# Python program to demonstrate
# find_one()


import pymongo


mystudent = pymongo.MongoClient('localhost', 27017)

# Name of the databse
mydb = mystudent["gfg"]

# Name of the collection
mycol = mydb["names"]

x = mycol.find_one()

print(x)
