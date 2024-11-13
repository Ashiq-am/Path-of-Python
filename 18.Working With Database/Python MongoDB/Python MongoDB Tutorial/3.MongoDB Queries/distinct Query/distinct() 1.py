# distinct() function returns the distinct values for the
# field dept from all documents in the mycollection collection
print(mycollection.distinct('dept'))

# distinct values for the field color,
# embedded in the field item, from all documents
# in the mycollection collection
print(mycollection.distinct('item.color'))

# returns the distinct values for the field sizes
# from all documents in the mycollection collection
print(mycollection.distinct("sizes"))

# distinct values for the field code,
# embedded in the field item, from the documents
# in mycollection collection whose dept is equal to B.
print(mycollection.distinct("item.code", {"dept" : "B"}))
