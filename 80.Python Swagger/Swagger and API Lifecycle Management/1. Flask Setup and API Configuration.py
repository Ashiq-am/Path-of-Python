from flask import Flask, request, send_file
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from PIL import Image
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Image Upload API',
          description='API for uploading and displaying images')
