import psycopg2
from config import config

conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**config)

    # Creating a cursor with name cur.
    cur = conn.cursor()

    # SQL query to fetch data from the database.
    cur.execute('SELECT * FROM BLOB_DataStore')

    # open(file,'wb').write() is used to
    # write the binary data to the file.
    for row in cur.fetchall():
        BLOB = row[2]
        open("new" + row[1], 'wb').write(BLOB)
        print(row[0], row[1], "BLOB Data is saved\
		in Current Directory")

    # Close the connection
    cur.close()

except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        # Commit the changes to the database
        conn.commit()
