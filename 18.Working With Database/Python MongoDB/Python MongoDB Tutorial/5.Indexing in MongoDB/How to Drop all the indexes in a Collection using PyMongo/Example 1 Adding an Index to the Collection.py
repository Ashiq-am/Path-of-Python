import pprint
import pymongo

# connection
try:
    client = pymongo.MongoClient()
    db = client['GFG']
    print('connection to the server established')

except Exception:
    print('Failed to Connect to server')

collection = db.lecture

# creating an index
resp = collection.create_index("l_id")

# printing the auto generated name
# returned by MongoDB
print(resp)

# index_information() is analogous
# to getIndexes
pprint.pprint(collection.index_information())
