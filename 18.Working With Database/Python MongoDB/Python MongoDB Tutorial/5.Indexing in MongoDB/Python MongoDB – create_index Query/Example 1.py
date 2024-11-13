from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['GFG']

# Access collection of the database
mycollection = mydatabase['College']

# Before Creating index
index_list = sorted(list(mycollection.index_information()))
print("Before Creating index")
print(index_list)

# Creating index
mycollection.create_index("student_id", unique=True)

# After Creating index
index_list = sorted(list(mycollection.index_information()))
print("\nAfter Creating index")
print(index_list)
