from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
