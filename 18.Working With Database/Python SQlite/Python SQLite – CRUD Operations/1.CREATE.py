# Python code to create a relation
# using SQLite3

# import the sqlite3 package
import sqlite3

# create a database named backup
cnt = sqlite3.connect("backup.dp")

# create a table named gfg
cnt.execute('''CREATE TABLE gfg(
NAME TEXT,
POINTS INTEGER,
ACCURACY REAL);''')
