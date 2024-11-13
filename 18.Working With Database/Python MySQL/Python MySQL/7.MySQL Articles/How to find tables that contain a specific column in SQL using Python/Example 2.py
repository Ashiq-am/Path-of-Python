# Module Imports
import mysql.connector as mariadb
import sys


# Connect to MariaDB Platform
try:
	conn = mariadb.connect(
		user="root",
		password="",
		database="gfg"
	)

except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)


# Get cursor object
cur = conn.cursor()


# Get the table and database details having a particular column
cur.execute("select tab.table_schema as database_name,tab.table_name "
            "from information_schema.tables as tab "
            "inner join information_schema.columns "
            "as col on col.table_schema = tab.table_schema "
            "and col.table_name = tab.table_name "
            "and column_name = 'Names' where tab.table_type = 'BASE TABLE' "
            "order by tab.table_schema, tab.table_name;")


# Display the tables
for(database_name, tab) in cur:
	print(f"\n\nTable Name: {tab}\nDatabase Name: {database_name}")
