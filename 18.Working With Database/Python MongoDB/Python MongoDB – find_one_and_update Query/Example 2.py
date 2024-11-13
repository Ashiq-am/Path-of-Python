from pymongo import MongoClient
from pymongo import ReturnDocument


# Create a pymongo client
client = MongoClient('localhost', 27017)

# Get the database instance
db = client['GFG']

# Create a collection
doc = db['Student']

print(# Increasing marks of Ravi by 10
doc.find_one_and_update({'name': "Raju"},
						{ '$set': { "Branch" : 'CSE'} },
						projection = { "name" : 1, "Branch" : 1 },
						return_document = ReturnDocument.AFTER))
