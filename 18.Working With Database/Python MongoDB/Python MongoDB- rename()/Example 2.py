# importing the module
from pymongo import MongoClient

# creating a MongoClient object
client = MongoClient()

# connecting with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# accessing the database
database = client['database']

# access collection of the database
mycollection = database['myTable']
docs = [{"id": 1, "name": "Drew"},
        {"id": 3, "name": "Cody"}]
mycollection.insert_many(docs)

# renaming the collection
mycollection.rename('collec', dropTarget=False)

result = database.collection_names()
for collect in result:
    print(collect)
