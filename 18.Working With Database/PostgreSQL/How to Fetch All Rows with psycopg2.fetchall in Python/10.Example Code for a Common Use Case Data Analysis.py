import psycopg2
import pandas as pd

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="business_data",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Execute a SELECT query to fetch transaction data
cur.execute("SELECT * FROM Transactions")

# Fetch all rows from the result set
rows = cur.fetchall()

# Convert the fetched data into a pandas DataFrame for analysis
columns = [desc[0] for desc in cur.description]  # Get column names from cursor description
df = pd.DataFrame(rows, columns=columns)

# Close the cursor and connection
cur.close()
conn.close()

# Perform data analysis using pandas (e.g., calculate total sales)
total_sales = df['amount'].sum()
print(f"Total Sales: {total_sales}")
