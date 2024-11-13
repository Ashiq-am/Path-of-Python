import pymongo


# establishing connection
# to the database
my_client = pymongo.MongoClient('localhost', 27017)

# Name of the databse
mydb = my_client["gfg"]

# Name of the collection
mynew = mydb["names"]


for x in my_client.find({}, {"_id":0, "name": 1, "address": 1 }):
    print(x)
