import psycopg2

# Define connection parameters
conn_params = {
    'dbname': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port',
   # or 'verify-ca', 'verify-full'
    'sslmode': 'require',
   # Required for 'verify-ca' and 'verify-full'
    'sslrootcert': '/path/to/ca_certificate.crt',
  # Optional, required for mutual authentication
    'sslcert': '/path/to/client_certificate.crt',
  # Optional, required for mutual authentication
    'sslkey': '/path/to/client_key.key'
}

# Establish a connection
conn = psycopg2.connect(**conn_params)

# Use the connection
# ...

# Close the connection
conn.close()
