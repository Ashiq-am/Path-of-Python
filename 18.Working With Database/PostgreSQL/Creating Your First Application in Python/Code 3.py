#!/usr/bin/python
import psycopg2

# Establish the connection to PostgreSQL
db_conn = psycopg2.connect("host=localhost dbname=test_db user=postgres password=5555")

#create a cursor object frpm connection modeul
cursor_object = db_conn.cursor()

# Add data into the test_names table of test_db
cursor_object.execute("INSERT INTO test_names (name) VALUES ('Ramadhir')")

# Save the changes to database
db_conn.commit()
