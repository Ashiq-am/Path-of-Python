import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["database"]

# Collection Name
col = db["GeeksForGeeks"]

x = col.find_one()

print(x)
