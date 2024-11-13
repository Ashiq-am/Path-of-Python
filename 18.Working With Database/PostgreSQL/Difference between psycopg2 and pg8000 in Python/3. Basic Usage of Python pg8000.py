import pg8000

# Establish a connection to the database
conn = pg8000.connect(
    database="GeeksData",
    user="your_username",
    password="your_password",
    host="localhost",
    port=5432
)

# Create a cursor object
cursor = conn.cursor()
