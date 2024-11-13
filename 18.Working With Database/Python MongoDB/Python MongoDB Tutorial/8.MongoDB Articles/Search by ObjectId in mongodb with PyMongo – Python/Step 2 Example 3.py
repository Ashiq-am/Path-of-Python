# search document with filter
# firat parameter is search queary
# second paramater is filter queary
# you can as many fields you want
# you can specify either 1 or 0
# in filter fields
# if you specify 0 the field will
# be eleminated form the result
queary = {"_id": ObjectId(id)}

filter = {"_id": 0}

collection.find_one(queary, filter)
