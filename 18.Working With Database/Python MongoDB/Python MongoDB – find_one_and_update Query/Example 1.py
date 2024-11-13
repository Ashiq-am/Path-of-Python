from pymongo import MongoClient
from pymongo import ReturnDocument


# Create a pymongo client
client = MongoClient('localhost', 27017)

# Get the database instance
db = client['GFG']

# Create a collection
doc = db['Student']

print(doc.find_one_and_update({'name':"Raju"},
						{ '$set': { "Branch" : 'ECE'} },
						return_document = ReturnDocument.AFTER))
