# importing the module
from pymongo import MongoClient, InsertOne, DeleteOne, ReplaceOne

# creating a MongoClient object
client = MongoClient()

# connecting with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# accessing the database
database = client['database']

# access collection of the database
mycollection = mydatabase['myTable']

# defining the requests
requests = [InsertOne({"Student name": "Cody"}),
            InsertOne({"Student name": "Drew"}),
            DeleteOne({"Student name": "Cody"}),
            ReplaceOne({"Student name": "Drew"},
                       {"Student name": "Andrew"}, upsert=True)]

# executing the requests
result = mycollection.bulk_write(requests)

for doc in mycollection.find({}):
    print(doc)
