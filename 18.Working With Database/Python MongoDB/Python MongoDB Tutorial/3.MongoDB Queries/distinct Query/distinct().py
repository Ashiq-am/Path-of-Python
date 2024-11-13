# importing the module
from pymongo import MongoClient

# creating a MongoClient object
client = MongoClient()

# connecting with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# accessing the database
database = client['database']

# access collection of the database
mycollection = mydatabase['myTable']

documents = [{"_id": 1, "dept": "A",
              "item": {"code": "012", "color": "red"},
              "sizes": ["S", "L"]},
             {"_id": 2, "dept": "A",
              "item": {"code": "012", "color": "blue"},
              "sizes": ["M", "S"]},
             {"_id": 3, "dept": "B",
              "item": {"code": "101", "color": "blue"},
              "sizes": "L"},
             {"_id": 4, "dept": "A",
              "item": {"code": "679", "color": "black"},
              "sizes": ["M"]}]

mycollection.insert_many(documents)
for doc in mycollection.find({}):
    print(doc)
