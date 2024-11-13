from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["library_management"]
students_collection = db["students"]
