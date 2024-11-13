import pandas, psycopg2

# Step 1: Setting Up PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="gfgdb",
    user="postgres",
    password="1234"
)
cursor = conn.cursor()

# Step 2: Reading Data from CSV
file = 'data.csv'
data = pandas.read_csv(file)
print(data.head())

# Step 3: Creating a employee Table in PostgreSQL
query = '''
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10)
);
'''
cursor.execute(query)
conn.commit()

# Step 4: Inserting Data into PostgreSQL
query = '''
INSERT INTO employee(name, age, gender)
VALUES (%s, %s, %s);
'''

for _, row in data.iterrows():
    cursor.execute(query, tuple(row))
conn.commit()

# Step 5: Verifying Data Migration
query = "SELECT * FROM employee;"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

# Closing the connection
cursor.close()
conn.close()
