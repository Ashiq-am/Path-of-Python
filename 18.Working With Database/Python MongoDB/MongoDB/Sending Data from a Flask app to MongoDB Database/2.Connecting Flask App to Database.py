from flask import Flask, request
from pymongo import MongoClient

# Flask app object
app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['demo']
collection = db['data']
