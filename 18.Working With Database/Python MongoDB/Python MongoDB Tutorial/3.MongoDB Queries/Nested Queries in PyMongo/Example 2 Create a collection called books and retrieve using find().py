import pprint
from pymongo import MongoClient
import datetime

client = MongoClient()
Database = client["GFG"]
books = Database["book"]

books.insert_many([
    {"author": "Samsuel", "book_id": 54, "ratings": 3,
     "publish": datetime.datetime(1999, 12, 6)},

    {"author": "Thomson", "book_id": 84, "ratings": 4,
     "publish": datetime.datetime(1996, 7, 12)},

    {"author": "Piyush Agarwal", "book_id": 34, "ratings": 1,
     "publish": datetime.datetime(2000, 9, 6)},

    {"author": "Shreya Mathur", "book_id": 12, "ratings": 2,
     "publish": datetime.datetime(2017, 8, 8)},

    {"author": "Antony Sharma", "book_id": 98, "ratings": 4,
     "publish": datetime.datetime(2003, 11, 5)},
])

# retrieving the documents
for x in books.find():
    pprint.pprint(x)
