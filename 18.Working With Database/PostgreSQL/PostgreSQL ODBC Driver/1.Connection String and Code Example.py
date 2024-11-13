import pyodbc

# ODBC driver PostgreSQL connexion_string = (    "Driver={PostgreSQL ODBC Driver};"    "Server=localhost;"    "Port=5432;"    "Database=testdb;"    "Uid=myusername;"    "Pwd=mypassword;"    "SSLmode=require;"    )
# Execute a simple SQL query
cursor.execute("SELECT * FROM employees;")
# Fetch all rows from the result set
rows = cursor.fetchall()
# Display the results
for row in rows:
    print(f"ID: {row.id}, Name: {row.name}, Position: {row.position}, Salary: {row.salary}")

except Exception as e:
print(f"An error occurred: {e}")
finally:
# Close the connection
if connection:
    connection.close()
