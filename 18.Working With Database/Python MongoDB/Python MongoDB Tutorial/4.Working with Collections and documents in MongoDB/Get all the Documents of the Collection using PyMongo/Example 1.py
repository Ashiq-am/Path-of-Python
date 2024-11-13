import pymongo

# establishing connection
# to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database name
db = client["mydatabase"]

# Collection name
col = db["gfg"]

# if we don't want to print id then pass _id:0
for x in col.find({}, {"_id": 0, "coursename": 1, "price": 1}):
    print(x)
