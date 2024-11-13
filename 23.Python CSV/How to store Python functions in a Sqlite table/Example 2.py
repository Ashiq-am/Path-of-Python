# Importing required library
import sqlite3

# Initializing the database
conn = sqlite3.connect('function.db')

# Creating cursor object
c = conn.cursor()

# Creating table
c.execute('''CREATE TABLE pyfuction (func_defination TEXT)''')

# Storing a python function in the Sqlite table
code = """ def add(): print((10+20)/2)"""
c.execute("INSERT INTO pyfuction (func_defination) VALUES (?)", (code,))

# Displaying Content of the table
c.execute("SELECT * FROM pyfuction;")
print(c.fetchall())

# Terminating the transaction
conn.commit()
