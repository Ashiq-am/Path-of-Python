# importing the modules
from pymongo import MongoClient, InsertOne, DeleteOne, ReplaceOne, UpdateOne

# creating a MongoClient object
client = MongoClient()

# connecting with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# accessing the database
database = client['database']

# access collection of the database
mycollection = mydatabase['myTable']

# defining the requests
requests = [InsertOne({"x": 5}),
            InsertOne({"y": 2}),
            UpdateOne({'x': 5}, {'$inc': {'x': 3}}),
            DeleteOne({"y": 2})]

# executing the requests
result = mycollection.bulk_write(requests)

for doc in mycollection.find({}):
    print(doc)
