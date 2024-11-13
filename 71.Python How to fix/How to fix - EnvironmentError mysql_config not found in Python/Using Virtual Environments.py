import mysql.connector

# Establishing a connection to MySQL
try:
    cnx = mysql.connector.connect(user='username', password='password',
                                  host='127.0.0.1',
                                  database='dbname')
    print("Connection successful!")
except mysql.connector.Error as err:
    print("Error:", err)
finally:
    # Closing the connection
    if 'cnx' in locals() or 'cnx' in globals():
        cnx.close()
        print("Connection closed.")
