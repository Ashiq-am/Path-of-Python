from pymongo import MongoClient

# Replace these with your MongoDB connection details
# MongoDB username
# MongoDB Password
# MongoDB hosting type
# Default port of MongoDB is 27017
# MongoDB Database name
MONGO_USERNAME = "sayantanbose"
MONGO_PASSWORD = "1992"
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "employee"

# Create a MongoDB client
client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}: {MONGO_PORT}/{MONGO_DB}")
db = client[MONGO_DB]
