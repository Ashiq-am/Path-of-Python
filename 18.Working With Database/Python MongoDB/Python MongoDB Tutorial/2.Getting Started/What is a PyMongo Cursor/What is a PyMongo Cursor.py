from pymongo import MongoClient

# Connecting to mongodb
client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.GFG
    lectures = db.lecture.find()

    print(lectures.next())
    print(lectures.next())
    print(lectures.next())

    print("\nRemaining Lectures\n")
    print(list(lectures))
