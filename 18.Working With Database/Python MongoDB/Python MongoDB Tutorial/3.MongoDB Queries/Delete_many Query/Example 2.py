import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connecting to the database
mydb = client["GFG"]

# Connecting the to collection
col = mydb["Geeks"]

query = {"Class": '3'}
d = col.delete_many(query)

print(d.deleted_count, " documents deleted !!")
