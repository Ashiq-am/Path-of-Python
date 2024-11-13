# import required modules
import sqlite3
from sqlite3 import Error as Err


# explicit function to connect database
# that resides in the memory
def SQLite_connection():
    try:
        # connect to the databse
        conn = sqlite3.connect('gfgdatabase.db')
        print("Database connection is established successfully!")

        # connect a database connection to the
        # database that resides in the memory
        conn = sqlite3.connect(':memory:')
        print("Established database connection to a database\
		that resides in the memory!")

    # if any interruption or error occurs
    except Err:
        print(Err)

    # terminate the connection
    finally:
        conn.close()


# function call
SQLite_connection()
