# Complete Function to Retrieve
# the BLOB data into the database.
import psycopg2
from config import config


# This Function will Creates File from binary data.
def Binary_To_File(BLOB, FileName, oldFileName):
    with open(f"{FileName}", 'wb') as file:
        file.write(BLOB)
    print(f"{oldFileName} File saved With Name name {FileName}")


def retrieve_BLOB(S_No, newFileName):
    """ Retrieve a BLOB From a table """
    conn = None
    try:
        # connect to the PostgreSQL server
        # & creating a cursor object
        conn = psycopg2.connect(**config)

        # Creating a cursor with name cur.
        cur = conn.cursor()

        # Retrieve BLOB data from the database.
        cur.execute('SELECT * FROM BLOB_DataStore')
        db = cur.fetchall()

        BLOB = db[S_No - 1][2]

        # open("FromDB"+db[0][1], 'wb').write(BLOB)
        Binary_To_File(BLOB, newFileName, db[S_No - 1][1])

        # Close the connection
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # Commit the changes to the database
            conn.commit()


retrieve_BLOB(1, 'OctaFromDB.jpg')
