from pymongo import MongoClient

# Create a pymongo client
client = MongoClient('localhost', 27017)

# database instance
db = client['GFG']

# collection instance
doc = db['Student']

# Retrieving 3 documents using the
# find() and limit() methods
print("3 docs in the collection are: ")

for doc1 in doc.find().limit(3).skip(2):
	print(doc1)
