import pymongo


connection = pymongo.MongoClient()
db = connection.GFG
col = db.lecture

# This is a cursor instance
cur = col.find()

if cur.count()==0:
	print("Empty Cursor")
else:
	print("Cursor is Not Empty")
	print("Do Stuff Here")
