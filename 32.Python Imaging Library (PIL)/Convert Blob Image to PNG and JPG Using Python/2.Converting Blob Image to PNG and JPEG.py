# Create a connection (Assuming you already have the connection setup)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="blob_image"
)

# Create a cursor object
cursor = mydb.cursor()

# Prepare the query
query = 'SELECT PICTURE FROM IMAGES WHERE ID=101'

# Execute the query to get the file
cursor.execute(query)
data = cursor.fetchall()

# The returned data will be a list of list
image_data = data[0][0]

# Decode the string
binary_data = base64.b64decode(image_data)

# Convert the bytes into a PIL image
image = Image.open(io.BytesIO(binary_data))

# Convert RGBA to RGB if the image has an alpha channel
if image.mode == 'RGBA':
    image = image.convert('RGB')

# Save the image as JPEG
image.save("output.jpg", "JPEG")

# Save the image as PNG
image.save("output.png", "PNG")
