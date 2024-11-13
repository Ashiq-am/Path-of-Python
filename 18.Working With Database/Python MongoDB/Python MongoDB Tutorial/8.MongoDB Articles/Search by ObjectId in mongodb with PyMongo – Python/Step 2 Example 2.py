# use the string object id
# and objectId object to
# create object of type ObjectId
id = "5fec2c0b348df9f22156cc07"
objInstance = ObjectId(id)

collection.find_one({"_id": objInstance})

# below line works same as the above
collection.find_one({"_id": ObjectId(id)})
collection.find_one(ObjectId(id))
