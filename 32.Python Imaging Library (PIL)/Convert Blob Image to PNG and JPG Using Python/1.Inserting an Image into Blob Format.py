import mysql.connector
import base64
from PIL import Image
import io

# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="blob_image"
)

# Create a cursor object
cursor = mydb.cursor()

# Open an image file in binary mode and read its contents
file = open('image.png', 'rb').read()

# Encode the file to get a base64 string
file = base64.b64encode(file)

# Sample data to be inserted
args = ('101', 'Sample Name', file)

# Prepare a query
query = 'INSERT INTO IMAGES VALUES (%s, %s, %s)'

# Execute the query and commit the database
cursor.execute(query, args)
mydb.commit()
