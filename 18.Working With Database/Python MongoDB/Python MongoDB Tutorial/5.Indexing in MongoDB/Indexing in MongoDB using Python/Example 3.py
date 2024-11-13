from pymongo import MongoClient, ASCENDING, DESCENDING

# Create a pymongo client
client = MongoClient('localhost', 27017)

# database instance
db = client['GFG']

# collection instance
doc = db['Student']

# Creating a compund field index in descending order
res = doc.create_index(
    [
        ("ascending_index", 1),
        ("second_descnding_indexed", DESCENDING)
    ]
)
print(res)
