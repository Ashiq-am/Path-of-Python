import psycopg

# Establish a connection to the database
with psycopg.connect(
    dbname="GeeksData",
    user="username",
    password="password",
    host="localhost",
    port="5432"
) as conn:
    # Create a cursor object
    with conn.cursor() as cursor:
        # Execute a SQL query
        cursor.execute("SELECT * FROM Geekstable")

        # Fetch one result
        result = cursor.fetchone()

        # Print the result
        print(result)
