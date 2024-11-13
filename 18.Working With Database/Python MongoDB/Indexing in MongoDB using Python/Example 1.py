from pymongo import MongoClient

# Create a pymongo client
client = MongoClient('localhost', 27017)

# database instance
db = client['GFG']

# collection instance
doc = db['Student']

# Creating a single field index
res = doc.create_index("index_created")
print(res)
