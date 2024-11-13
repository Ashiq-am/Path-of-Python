# Python code to illustrate
# Replace_many() in MongoDB
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

# replace one of the employee data whose name is Mr.Shaurya
result = collection.replace_many(
    {"eid": 14},
    {
        "name": "Mr.GfG",
        "eid": 45,
        "location": "noida"

    }
)

print("Data replaced with id", result)

# Print the new record
cursor = collection.find()
for record in cursor:
    print(record)
