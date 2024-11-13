import pymongo


# establishing connection
# to the database
my_client = pymongo.MongoClient('localhost', 27017)

# Name of the databse
mydb = my_client["gfg"]

# Name of the collection
mynew = mydb["names"]

# sorting function with -1
# as direction
mydoc = mynew.find().sort("name", -1)

for x in mydoc:
	print(x)
