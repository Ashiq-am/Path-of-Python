# import mysql-connector to connect MySQL server
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
)

# check if connected or not
print(conn)

# disconnect to server
conn.close()
