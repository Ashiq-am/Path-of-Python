# import libraries
from flask import Flask, render_template, request
from newsapi import NewsApiClient

# init flask app
app = Flask(__name__)

# Init news api
newsapi = NewsApiClient(api_key='YOUR_API_KEY')
