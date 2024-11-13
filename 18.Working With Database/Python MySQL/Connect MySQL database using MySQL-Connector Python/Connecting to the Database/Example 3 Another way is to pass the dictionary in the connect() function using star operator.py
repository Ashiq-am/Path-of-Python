# Python program to connect
# to mysql databse


from mysql.connector import connection


dict = {
'user': 'root',
'host': 'localhost',
'database': 'College'
}

# Connecting to the server
conn = connection.MySQLConnection(**dict)

print(conn)

# Disconnecting from the server
conn.close()
