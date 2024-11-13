import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
)

# creating cursor object
cursor = conn.cursor()

# creating database
cursor.execute("CREATE DATABASE GFG")
