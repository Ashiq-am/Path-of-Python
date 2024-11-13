# Python program to connect
# to mysql databse


from mysql.connector import connection

# Connecting to the server
conn = connection.MySQLConnection(user = 'username',
							host = 'localhost',
							database = 'database_name')

print(conn)

# Disconnecting from the server
conn.close()
