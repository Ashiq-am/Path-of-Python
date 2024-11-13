import psycopg2

# Using a context manager to handle connection
with psycopg2.connect(
    dbname="yourdbname",
    user="yourusername",
    password="yourpassword",
    host="yourhost",
    port="yourport"
) as conn:
    # Perform database operations
    # ...
    pass  # Connection is automatically closed here
