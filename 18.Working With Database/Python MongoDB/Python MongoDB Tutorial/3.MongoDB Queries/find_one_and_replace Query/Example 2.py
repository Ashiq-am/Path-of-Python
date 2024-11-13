import pymongo

# establishing connection
# to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database name
db = client["mydatabase"]

# Collection name
col = db["gfg"]

# replce with the help of
# find_one_and_replace()
col.find_one_and_replace({'price': 9999}, {'price': 19999})

# print the document after replacement
for x in col.find({}, {"_id": 0, "coursename": 1, "price": 1}):
    print(x)
