import psycopg2

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    dbname="mydatabase",
    user="username",
    password="password",
    host="localhost"
)
cursor = connection.cursor()

# Create the users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
""")
connection.commit()

# Insert a new user
cursor.execute("""
    INSERT INTO users (name, email)
    VALUES (%s, %s)
""", ('John Doe', 'john.doe@example.com'))
connection.commit()

# Query the user
cursor.execute("SELECT email FROM users WHERE name = %s", ('John Doe',))
user_email = cursor.fetchone()[0]
print(user_email)

# Close the connection
cursor.close()
connection.close()
