from pymongo import MongoClient

my_client = MongoClient('localhost', 27017)
db = my_client["GFG"]
coll = db["Student"]

# Aggregation
cursor = coll.aggregate([{"$group":
	{"_id":"$None",
	"total collections":{"$sum": 1}
	}
	}])

for document in cursor:
	print(document)
