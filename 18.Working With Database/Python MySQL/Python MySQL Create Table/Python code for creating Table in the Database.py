# Python code for creating Table in the Database
# Host: It is the server name. It will be "localhost"
# if you are using localhost database

import mysql.connector as SQLC


def CreateTable():
    # Connecting To the Database in Localhost
    DataBase = SQLC.connect(
        host="server name",
        user="user name",
        password="password",
        database="College"
    )

    # Cursor to the database
    Cursor = DataBase.cursor()

    # Query for Creating the table
    # The student table contains two columns Name and
    # Roll number of data types varchar i.e to store string
    # and Roll number of the integer data type.
    TableName = """CREATE TABLE Student(Name VARCHAR(255),Roll_no int)"""


    Cursor.execute(TableName)
    print("Student Table is Created in the Database")
    return

# Calling CreateTable function
CreateTable()

