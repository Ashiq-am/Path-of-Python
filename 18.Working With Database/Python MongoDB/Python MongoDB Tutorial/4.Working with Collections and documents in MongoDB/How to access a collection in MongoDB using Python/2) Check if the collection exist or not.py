from pymongo import MongoClient


# create an client instance of
# the MongoDB class
mo_c = MongoClient()

# create an instance of 'some_database'
db = mo_c.GFG

# check collection is exists or not
print(hasattr(db, 'Geeks'))
