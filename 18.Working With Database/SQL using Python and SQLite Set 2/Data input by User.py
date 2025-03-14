# code for executing query using input data
import sqlite3

# creates a database in RAM
from pip._vendor.distlib.compat import raw_input

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table person (name, age, id)")

print ("Enter 5 students names:")
who = [raw_input() for i in range(5)]
print ("Enter their ages respectively:")
age = [int(raw_input()) for i in range(5)]
print ("Enter their ids respectively:")
p_id = [int(raw_input()) for i in range(5)]
n = len(who)

for i in range(n):

	# This is the q-mark style:
	cur.execute("insert into person values (?, ?, ?)", (who[i], age[i], p_id[i]))

	# And this is the named style:
	cur.execute("select * from person")

	# Fetches all entries from table
	print(cur.fetchall())
