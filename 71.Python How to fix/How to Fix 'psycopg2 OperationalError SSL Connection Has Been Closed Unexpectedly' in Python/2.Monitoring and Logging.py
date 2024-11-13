import logging

logging.basicConfig(level=logging.INFO)
try:
    connection = psycopg2.connect(
        dbname="testdb",
        user="user",
        password="password",
        host="localhost",
        port="5432",
        sslmode="require"
    )
    logging.info("Database connection established")
except psycopg2.OperationalError as e:
    logging.error(f"Connection error: {e}")
