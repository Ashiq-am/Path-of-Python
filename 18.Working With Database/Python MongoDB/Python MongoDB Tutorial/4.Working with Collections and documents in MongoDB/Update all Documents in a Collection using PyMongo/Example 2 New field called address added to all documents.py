from pymongo import MongoClient

# Creating an instance of MongoClient
# on default localhost
client = MongoClient('mongodb://localhost:27017')

# Accessing desired database and collection
db = client.gfg
collection = db["classroom"]

# Address filed to be added to all documents
collection.update_many(
    {},
    {"$set":
        {
            "Address": "value"
        }
    },

    # don't insert if no document found
    upsert=False,
    array_filters=None
)
