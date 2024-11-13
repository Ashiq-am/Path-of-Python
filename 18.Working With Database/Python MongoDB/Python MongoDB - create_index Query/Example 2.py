from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['GFG']

# Access collection of the database
mycollection = mydatabase['College']

record = {'_id': 4,
          "student_id": 873,
          "name": "John",
          "section": "A"}

mycollection.insert_one(record)
