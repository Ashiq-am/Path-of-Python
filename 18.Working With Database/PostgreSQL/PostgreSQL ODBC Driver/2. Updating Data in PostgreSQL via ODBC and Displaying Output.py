import pyodbc

# Connection string for PostgreSQL ODBC driver
connection_string = (
    "Driver={PostgreSQL ODBC Driver};"
    "Server=localhost;"
    "Port=5432;"
    "Database=testdb;"
    "Uid=myusername;"
    "Pwd=mypassword;"
    "SSLmode=require;"
)

try:
    # Establishing connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Display current data
    print("Current Employee Data:")
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row.id}, Name: {row.name}, Position: {row.position}, Salary: {row.salary}")

    # Update an employee's salary
    update_query = "UPDATE employees SET salary = salary + 5000 WHERE name = ?;"
    cursor.execute(update_query, ('Jane Smith',))
    connection.commit()  # Commit changes to the database

    # Display updated data
    print("\nUpdated Employee Data:")
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row.id}, Name: {row.name}, Position: {row.position}, Salary: {row.salary}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if connection:
        connection.close()
