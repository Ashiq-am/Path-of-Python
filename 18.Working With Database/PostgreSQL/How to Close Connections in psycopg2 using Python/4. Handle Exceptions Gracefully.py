import psycopg2
from psycopg2 import sql

# Database connection parameters
dbname = "yourdbname"
user = "yourusername"
password = "yourpassword"
host = "yourhost"
port = "yourport"


def connect_and_query():
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Create a cursor object using the connection
        with conn.cursor() as cur:
            # Define a simple SQL query
            query = sql.SQL("SELECT version();")

            # Execute the query
            cur.execute(query)

            # Fetch the result
            result = cur.fetchone()
            print("Database Version:", result[0])

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Ensure the connection is closed
        if conn is not None:
            conn.close()
            print("Connection closed.")


# Run the function
connect_and_query()
