from pymongo import MongoClient

# Create a pymongo client
client = MongoClient('localhost', 27017)

# database instance
db = client['GFG']

# collection instance
doc = db['Student']

# Printing documents of only those having
# branch as CSE and limiting the document
# to 1
for doc1 in doc.find({'Branch': 'CSE'}).limit(1):
	print(doc1)
