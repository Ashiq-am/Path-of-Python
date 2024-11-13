# import sqlite3 module
import sqlite3

# create con object to connect
# the database geeks_db.db
con = sqlite3.connect("geeks_db.db")

# create the cursor object
cur = con.cursor()

# execute the script by creating the
# table named geeks_demo and insert the data
cur.executescript("""
	create table geeks_demo(
		geek_id,
		geek_name
	);
insert into geeks_demo values ( '7058', 'sravan kumar' );
insert into geeks_demo values ( '7059', 'Jyothika' );
insert into geeks_demo values ( '7072', 'Harsha' );
insert into geeks_demo values ( '7075', 'Deepika' );

	""")

# display the data in the table by
# executing the cursor object
cur.execute("SELECT * from geeks_demo")

# fetch all the data
print(cur.fetchall())
