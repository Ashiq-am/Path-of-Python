from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['database4']

# Access collection of the database
mycollection = mydatabase['myTable']
writer_profiles = [
    {"_id": 1, "user": "Amit", "title": "Python", "comments": 8},
    {"_id": 2, "user": "Drew", "title": "JavaScript", "comments": 15},
    {"_id": 3, "user": "Amit", "title": "C++", "comments": 6},
    {"_id": 4, "user": "Drew", "title": "MongoDB", "comments": 2},
    {"_id": 5, "user": "Cody", "title": "MongoDB", "comments": 16}]

mycollection.insert_many(writer_profiles)
agg_result = mycollection.aggregate(
    [{
        "$group":
            {"_id": "$title",
             "total": {"$sum": 1}
             }}
    ])
for i in agg_result:
    print(i)
