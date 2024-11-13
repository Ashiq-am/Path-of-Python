import pprint
from pymongo import MongoClient


client = MongoClient()

Database = client["GFG"]
lecturers = Database["lecture"]

lecturers.insert_many([
{"l_id":56, "d_id":1, "salary":50000},
{"l_id":57, "d_id":3, "salary":40000},
{"l_id":58, "d_id":4, "salary":90000},
{"l_id":59, "d_id":2, "salary":50000},
{"l_id":52, "d_id":1, "salary":70000},
{"l_id":53, "d_id":5, "salary":30000}
])

# retrieving the documents
for x in lecturers.find():
	pprint.pprint(x)
