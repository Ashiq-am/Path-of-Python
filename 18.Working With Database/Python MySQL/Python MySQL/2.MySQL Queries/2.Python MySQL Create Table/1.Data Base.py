# Python code for creating Database
# Host: It is the server name. It will be
# "localhost" if you are using localhost database

import mysql.connector as SQLC
# Establishing connection with the SQL

DataBase = SQLC.connect(
host ="server name",
user ="user name",
password ="password"
)
# Cursor to the database
Cursor = DataBase.cursor()

Cursor.execute("CREATE DATABASE College")
print("College Data base is created")
