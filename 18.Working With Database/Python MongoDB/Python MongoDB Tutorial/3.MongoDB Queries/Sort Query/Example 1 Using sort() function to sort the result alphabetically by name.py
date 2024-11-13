# python code to sort elements
# alphabetically in ascending order

import pymongo


# establishing connection
# to the database
my_client = pymongo.MongoClient('localhost', 27017)

# Name of the databse
mydb = my_client["gfg"]

# Name of the collection
mynew = mydb["names"]

# sorting function
mydoc = mynew.find().sort("name")

for x in mydoc:
	print(x)
