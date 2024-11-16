# Import the required libraries
import sqlite3
import pandas

# Prepare a connection object
# Pass the Database name as a parameter
conn = sqlite3.connect("Novels.db")

# Use read_sql_query method
# Pass SELECT query and connection object as parameter
pdSql = pd.read_sql_query("SELECT * FROM novels", conn)

# Print the dataframe object
print(pdSql)

# Close the connection object
conn.close()
