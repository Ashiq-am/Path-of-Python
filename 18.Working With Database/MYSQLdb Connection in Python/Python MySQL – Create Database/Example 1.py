# importing rquired libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="user",
passwd ="gfg"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE geeks4geeks")









"""The above program illustrates the creation of MySQL database geeks4geeks in which host-name is localhost, 
the username is user and password is gfg."""
