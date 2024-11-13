import psycopg2
from psycopg2 import sql

# Define connection parameters
conn_params = {
    'dbname': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port',
  # Options: disable, require, verify-ca, verify-full
    'sslmode': 'verify-full',
  # Required for verify-ca and verify-full
    'sslrootcert': '/path/to/ca_certificate.crt',
   # Required for client authentication (if needed)
    'sslcert': '/path/to/client_certificate.crt',
  # Required for client authentication (if needed)
    'sslkey': '/path/to/client_key.key'
}

# Establish a connection
try:
    conn = psycopg2.connect(**conn_params)
    print("Connection established successfully.")

    # Create a cursor object
    cur = conn.cursor()

    # Execute a simple query
    cur.execute(sql.SQL("SELECT version();"))

    # Fetch and print the result
    db_version = cur.fetchone()
    print(f"Database version: {db_version}")

    # Close the cursor and connection
    cur.close()
    conn.close()
    print("Connection closed.")

except psycopg2.Error as e:
    print(f"An error occurred: {e}")
