import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database name
db = client["GFG"]

# Collection name
col = db["gfg"]

# Query to be updated
query = { "coursename": "SYSTEM DESIGN" }

# New value
newvalue = { "$set": { "coursename": "Computer network" } }

# Update the value
col.update_many(query, newvalue)
