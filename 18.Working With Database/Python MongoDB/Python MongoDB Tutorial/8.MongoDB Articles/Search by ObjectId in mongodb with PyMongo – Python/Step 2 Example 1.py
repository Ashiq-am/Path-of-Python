# inserts data into collection and
# returns an object of type objectId
objInstance = collection.insert_one({"name": "sam", "age": 20}).inserted_id

# search MongoDB with
# an object of type objectId
collection.find_one(objInstance)
