from flask import Flask
from pymongo import MongoClient
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
