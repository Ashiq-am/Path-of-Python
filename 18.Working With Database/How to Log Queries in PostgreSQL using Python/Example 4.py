import logging
import psycopg2
from psycopg2.extras import LoggingConnection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("loggerinformation")

# We need to specify the necessary parameters in the below list
# As connecting with postgres/password as username/password and with testdb as parameters
db_settings = {
	"user": "postgres",
	"password": "password",
	"host": "127.0.0.1",
	"database": "testdb",
}

# connect to the PostgreSQL server
conn = psycopg2.connect(connection_factory=LoggingConnection, **db_settings)
conn.initialize(logger)

cur = conn.cursor()
cur.execute("SELECT * FROM employee")
