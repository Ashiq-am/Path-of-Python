# Python code to illustrate
# updating data in MongoDB
# with Data of employee with id:24
from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.database

# Created or Switched to collection names: my_gfg_collection
collection = db.my_gfg_collection

# update all the employee data whose eid is 24
result = collection.update_many(
    {"eid": 24},
    {
        "$set": {
            "name": "Mr.Geeksforgeeks"
        },
        "$currentDate": {"lastModified": True}

    }
)

print("Data updated with id", result)

# Print the new record
cursor = collection.find()
for record in cursor:
    print(record)
