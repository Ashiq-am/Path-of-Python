import logging
import psycopg2
from psycopg2.extras import LoggingConnection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("loggerinformation")

db_settings = {
	"user": "postgres",
	"password": "password",
	"host": "127.0.0.1",
	"database": "testdb",
}

conn = psycopg2.connect(connection_factory=LoggingConnection, **db_settings)
conn.initialize(logger)

cur = conn.cursor()
cur.execute("SELECT * FROM employee")

# insert records in employee table
cur.execute("INSERT INTO employee (first_name,last_name,age,gender,income) VALUES ('123','456',20,'m',20000)")
